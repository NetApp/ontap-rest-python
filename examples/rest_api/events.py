#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies.
This script is not officially supported as a
standard NetApp product.

Purpose: This Module covers 3 usecases in events Management using ONTAP REST API
1. View count of events info
2. Retrive events registered with specific severity and specific message:
3. Workflow: Create a event configuration --->
    Create a filter with rules --->
    Send destination notification.
Usage: events.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
events.py: the following arguments are required: -c/--cluster, -u/--admin, -p/--password

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import sys
import base64
import argparse
from getpass import getpass
import logging
import texttable as tt
import requests
from dateutil.parser import parse
import urllib3 as ur
# requests.packages.urllib3.

ur.disable_warnings()


def get_method_call_sever(cluster: str, headers_inc: str):
    """Get events with specific message pattern and severity"""
    message_name = input(
        "Enter the message pattern you want to view: [e.g:*call*, csm.*] : ")
    message_severity = input(
        "Enter the message severity [e.g: emergency, alert, debug ]: ")
    url = "https://{}/api/support/ems/events/?message.name={}&message.severity={}".format(
        cluster, message_name, message_severity)
    print(url)
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()


def get_method_call(cluster: str, max_records: int, headers_inc: str):
    """Get particular no of events"""
    url = "https://{}/api/support/ems/events/?max_records={}".format(
        cluster, max_records)
    print(url)
    response = requests.get(url, headers=headers_inc, verify=False)
    return response.json()


def get_events(cluster: str, headers_inc: str, answer: int):
    "Display events call output"
    ctr = 0
    print()
    if answer == '1':
        max_records = input(
            "\n Input the no of events you would like to view [e.g 1,10,100]:  ")
        tmp = dict(get_method_call(cluster, max_records, headers_inc))
    if answer == '2':
        tmp = dict(get_method_call_sever(cluster, headers_inc))
    vols = tmp['records']
    tab = tt.Texttable()
    header = ['Events name', 'Time', 'Severity']
    tab.header(header)
    tab.set_cols_align(['c', 'c', 'c'])
    for eventlist in vols:
        ctr = ctr + 1
        vol = eventlist['log_message']
        eve = eventlist['time']
        eve = parse(eve)
        sev = eventlist['message']['severity']
        row = [vol, eve, sev]
        tab.set_cols_width([55, 30, 20])
        tab.add_row(row)
        tab.set_cols_align(['c', 'i', 'c'])
    setdisplay = tab.draw()
    print(setdisplay)
    print("\n Number of Events displayed: {}".format(ctr))


def get_ems_config(cluster: str, headers_inc: str):
    """Fetches the EMS configuration"""
    url = "https://{}/api/support/ems/".format(cluster)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    tmp = dict(response.json())
    print("\nEMS Configuration:- ")
    print("=====================")
    print("Mail_from = %s " % tmp['mail_from'])
    print("Mail_server = %s " % tmp['mail_server'])
    print("=====================")


def patch_ems_config(cluster: str, headers_inc: str):
    """Code to perform event configuration modification"""
    print("EMS Event Config Modify")
    print("=========================")
    dataobj = {}
    snapbool = input("Would you like to update the Mail from Value: (y/n): ")
    if snapbool == 'y':
        mail_from = input(
            "Enter the  Mail from value [e.g: admin@mycompany.com] : ")
        dataobj['mail_from'] = mail_from
    combool = input("Would you like to update the Mail server (y/n): ")
    if combool == 'y':
        mailserver = input(
            "Enter the mail Server [e.g: mail@mycompany.com] : ")
        dataobj['mail_server'] = mailserver
    url = "https://{}/api/support/ems/".format(cluster)
    print()
    print(url)
    print("\n Passing input values:")
    print(dataobj)
    try:
        response = requests.patch(
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
    print("\nEMS Configuration done successfully \n")
    get_ems_config(cluster, headers_inc)


def create_filter(cluster: str, headers_inc: str):
    """To create a new filter with specific rules by user"""
    print()
    print("Create Filters")
    print("=============================================")

    filter_name = input("Enter the filter name :-")
    name_pattern = input("Enter Message name filter on which to match:")
    severities = input(
        "Enter Severities [e.g: Error,Emergency,Alert,Informational,Debug]:")
    type_input = input("Enter the Rule type [e.g: include or exclude]:")
    print()
    dataobj = {}
    dataobj = {"name": filter_name, "rules": [{"message_criteria": {
        "name_pattern": name_pattern, "severities": severities}, "type": type_input}]}
    print(dataobj)
    url = "https://{}/api/support/ems/filters/".format(cluster)
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
    print("\n Filter %s created Successfully:" % filter_name)


def destination_notify(cluster: str, headers_inc: str):
    """ Create Event Destination to send Notifications"""
    print("\nCreate Destination config details")
    print("=============================================")
    destination_name = input(
        "Enter the Event Destination name (e.g: admin_email):-")
    destination = input(
        "Enter the Event Destination [e.g: admin@domain.com] :-")
    filter_name = input(
        "Enter the filter name to get notified for [e.g: important-events]: ")
    dest_type = input(
        "Enter the type of notification [e.g: snmp, email, syslog, rest_api]: ")
    dataobj = {}
    dataobj = {"destination": destination, "filters": [{"name": filter_name}],
               "name": destination_name, "type": dest_type}
    print(dataobj)
    url = "https://{}/api/support/ems/destinations/".format(cluster)
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
    print()
    print("\n Event Destination created Successfully to send notification")


def events_management(cluster: str, headers_inc: str):
    """Module to cover the 3 usecases"""
    print("\n")
    print("=======================================================")
    print("This Module covers 3 usecases in Events Management")
    print("=======================================================")
    value = 'y'
    while value == 'y':
        print("\n 1. View count of Events info")
        print(
            "\n 2. Retrive events registered with specific severity and specific message:")
        print("\n3. Workflow: ")
        print("  Create a Event configuration")
        print("  -> Create a filter with rules")
        print("     -> Send destination notification")
        option = input("\nEnter your option [e.g:2]: ")
        if option == '1':
            get_events(cluster, headers_inc, option)
        if option == '2':
            get_events(cluster, headers_inc, option)
        if option == '3':
            patch_ems_config(cluster, headers_inc)
            create_filter(cluster, headers_inc)
            destination_notify(cluster, headers_inc)
        value = input("\n To continue press 'y' to exit press 'n':")
    print("\n")


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will list volumes in a SVM")
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details")
    parser.add_argument(
        "-u",
        "--api_user",
        default="admin",
        help="API Username")
    parser.add_argument("-p", "--api_pass", help="API Password")
    parsed_args = parser.parse_args()
    # collect the password without echo if not already provided
    if not parsed_args.api_pass:
        parsed_args.api_pass = getpass()

    return parsed_args


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )
    ARGS = parse_args()
    BASE64STRING = base64.encodestring(
        ('%s:%s' %
         (ARGS.api_user, ARGS.api_pass)).encode()).decode().replace('\n', '')

    headers = {
        'authorization': "Basic %s " % BASE64STRING,
        'content-type': "application/json",
        'accept': "application/json"
    }
    events_management(ARGS.cluster, headers)
    print("========= END OF MODULE ============")
