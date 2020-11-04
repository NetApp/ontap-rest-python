#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS WORKFLOW CREATING NEW SCHEDULE AND GETTING POLICIES

usage: python3 schedules_policies_sm_relationship.py [-h] -c CLUSTER [-u API_USER]
                                        [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import requests
import texttable as tt
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection
ur.disable_warnings()


def create_schedules(
        cluster: str,
        headers_inc: str):
    """ Create schedules at cluster at Cluster level"""
    print("\nThe List of SVMs")
    schedule_name = input("Schedule_name : ")
    type_value = input("Enter the type cron or interval? : ")
    if type_value == 'cron':
        hours = input("Hours? *[0-23]: ")
        minutes = input("Minutes? *[0-59] : ")
        days = input("Days? *[1-31] :  ")
        months = input("Months? *[1-12] :  ")
        weekdays = input("weekdays? *[0-6] :  ")
        tmp4 = {
            "hours": [hours],
            "minutes": [minutes],
            "days": [days],
            "months": [months],
            "weekdays": [weekdays]}
        dataobj = {
            "name": schedule_name,
            "cron": tmp4}
    if type_value == 'interval':
        interval = input(
            "\nEnter the interval (An ISO-8601 duration formatted string e.g: P1DT2H3M4S): ")
        dataobj = {
            "name": schedule_name,
            "interval": interval}
        print(dataobj)

    url = "https://{}/api/cluster/schedules".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
            verify=False)
        print(response)
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

    url_text = response.json()
    print("\n Schedule {} created successfully".format(schedule_name))


def get_policy(cluster: str, headers_inc: str):
    """ Get Policies at Cluster level"""

    url = "https://{}/api/snapmirror/policies?fields=*".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
        print(response)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = dict(response.json())
    if 'error' in url_text:
        print(url_text)
    vols = url_text['records']
    tab = tt.Texttable()
    header = [
        'Name',
        'UUID',
        'Scope',
        'Type']
    tab.header(header)
    tab.set_cols_align(['c', 'c', 'c', 'c'])
    ctr = 0
    for eventlist in vols:
        ctr = ctr + 1
        eve = eventlist['name']
        sev = eventlist['uuid']
        har = eventlist['scope']
        per = eventlist['type']
        row = [eve, sev, har, per]
        tab.set_cols_width([15, 30, 15, 15])
        tab.add_row(row)
        tab.set_cols_align(['c', 'c', 'c', 'c'])
    setdisplay = tab.draw()
    print(setdisplay)
    print("\nThe total no of Policies : ", ctr)


def schedule_policies(cluster, headers_inc) -> None:
    """Creation of new schedule and retrieving policies"""
    loop = 'y'
    while loop == 'y':
        print("==============================================================")
        print("\n1) Creation of schedules \n2) Get Policies")
        print("==============================================================")
        volumebool = input(
            "\n Which operation would you like to do [e.g. 1,2,3]?: ")
        if volumebool == '1':
            create_schedules(cluster, headers_inc)
        if volumebool == '2':
            get_policy(cluster, headers_inc)
        loop = input("\n To continue press 'y' to exit press 'n':")
    print("\n")


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Schedules and Policies using ONTAP REST APIs.",
        arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    schedule_policies(args.cluster, headers)


if __name__ == "__main__":
    main()
