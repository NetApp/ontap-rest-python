#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS PORTSET OPERATIONS USING REST API.

usage: python3 portset_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import json
import sys
import requests
import texttable as tt
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection
from utils import show_svm
ur.disable_warnings()


def list_portsets(cluster: str, headers_inc: str):
    """ Retrieving summary of all portsets in the cluster"""
    print()
    print("=======================================")
    print("Getting Portset Summary in the cluster")
    print("=======================================")
    api_url = "https://{}/api/protocols/san/portsets".format(
        cluster)
    try:
        response = requests.get(
            api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tsdict = dict(response.json())
    values = tsdict['records']
    print()
    for data in values:
        print("PortSet Name: %s" % (data['name']))
        print("Portset UUID: %s" % (data['uuid']))
        print()

def list_specific_portsets(cluster: str, headers_inc: str, portset_id: str):
    """ Retrieving specific details of a portset in the cluster"""
    print()
    print("=======================================")
    print("Getting Specific Portset details in the cluster")
    print("=======================================")
    api_url = "https://{}/api/protocols/san/portsets//{}/interfaces".format(
        cluster, portset_id)
    try:
        response = requests.get(
            api_url,
            headers=headers_inc,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tsdict = dict(response.json())
    values = tsdict['records']
    print()
    print(json.dumps(response.json(), indent=4))
    print("Trying texttable")
    ctr = 0
    tab = tt.Texttable()
    header = ['Protocol Type', 'Name', 'UUID']
    tab.header(header)
    tab.set_cols_align(['c', 'c', 'c'])
    for eventlist in values:
        ctr = ctr + 1
        vol = eventlist['protocol']
        eve = eventlist['ip']['name']
        #eve = parse(eve)
        sev = eventlist['ip']['uuid']
        row = [vol, eve, sev]
        tab.set_cols_width([55, 30, 20])
        tab.add_row(row)
        tab.set_cols_align(['c', 'i', 'c'])
    setdisplay = tab.draw()
    print(setdisplay)
    print("\n Number of interfaces in this portset: {}".format(ctr))

def delete_portset(cluster: str, headers_inc: str, uuid: str):
    """ portset delete module"""
    print("=============================================")
    print()
    urlpath = "https://{}/api/protocols/san/portsets/{}/"
    url = urlpath.format(cluster, uuid)
    try:
        response = requests.delete(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    print(".........Portset deleted successfully........")
    list_portsets(cluster, headers_inc)

def create_portset(cluster: str, headers_inc: str):
    """ create portset without interfaces"""
    print("=============================================")
    print()
    show_svm(cluster, headers_inc)
    print()
    svm_name = input("Enter the SVM :- ")
    print()
    name_portset = input("Enter a name for Portset Creation :- ")
    protocol_type = input(" Enter type of protocol [ fcp, iscsi, mixed ]:- ")
    print()
    dataobj = {}
    dataobj['svm'] = svm_name
    #dataobj['uuid'] = svm_key
    dataobj['name'] = name_portset
    dataobj['protocol'] = protocol_type

    print(dataobj)
    url = "https://{}/api/protocols/san/portsets".format(
        cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    list_portsets(cluster, headers_inc)
    add_interface(cluster, headers_inc)


def add_interface(cluster: str, headers_inc: str):
    """ create portset with interfaces"""
    print("====================Add interface=========================")
    uuid = input("Enter UUID of Portset :- ")
    protocol_type = input(" Enter name of protocol [ fc, iscsi ]:- ")
    lif_name = input("Enter a lif_name to add :- ")
    dataobj = {}
    dataobj = {protocol_type: {"name": lif_name}}
    print(dataobj)
    url = "https://{}/api/protocols/san/portsets/{}/interfaces".format(
        cluster, uuid)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(str(err))
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(err))
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    list_specific_portsets(cluster, headers_inc, uuid)


def portset_ops(cluster: str, headers_inc: str):
    """Demonstrates Portset Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS PORTSET OPERATIONS USING REST API.")
    print("==================================================================")
    print("Choose the Portset operation?")
    print("\n1.list \n2.create \n3.update \n4.delete \n5.Details of specific portset")
    snapshotbool = input(
        " \n\n enter option [e.g: 1]: ")
    if snapshotbool == '1':
        list_portsets(cluster, headers_inc)
    if snapshotbool == '2':
        create_portset(cluster, headers_inc)
    if snapshotbool == '3':
        add_interface(cluster, headers_inc)
    if snapshotbool == '4':
        list_portsets(cluster, headers_inc)
        portset_uuid = input ("enter uuid of specific portset: ")
        delete_portset(cluster, headers_inc, portset_uuid)
    if snapshotbool == '5':
        list_portsets(cluster, headers_inc)
        portset_uuid = input ("enter uuid of specific portset: ")
        list_specific_portsets(cluster, headers_inc, portset_uuid)

def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Portset Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    portset_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
