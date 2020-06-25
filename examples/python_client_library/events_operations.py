"""
ONTAP REST API Python Sample Scripts
This script was developed by NetApp to help demonstrate
NetApp technologies. This script is not officially
supported as a standard NetApp product.
Purpose: This script will enable certificate authentication on the provided account (or admin)
usage: events_operations.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
workflow:
    1. List EMS Config
    2. List EMS Destination
    2. Create a new test role and a test account and assign the account to the role
    3. Call an allowed API, expect success, modify role, re-call API, expect failure
    4. Delete the test roll and test account
Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New or Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import pprint
from netapp_ontap.error import NetAppRestError
from netapp_ontap.resources import (
    EmsDestination,
    EmsConfig,
    EmsEvent,
    EmsFilter,
    EmsFilterRule,
)
from utils import Argument, substep, parse_args, setup_connection, setup_logging


def show_emsconfig() -> None:
    """Show EMS Config"""

    substep("EMS Config")
    print("======================")
    try:
        emsconfig = EmsConfig()
        emsconfig.get()
        print("EmsConfig Name = %s" % emsconfig)
        print("Mail Server = %s" % emsconfig.mail_server)
        print("Mail From = %s" % emsconfig.mail_from)
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_emsdestination() -> None:
    """Show EMS Config"""

    substep("EMS Destination")
    print("======================")
    try:
        emsdestination = EmsDestination.get_collection()
        for emsdestination in EmsDestination.get_collection():
            print("=====")
            pprint.pprint(emsdestination.to_dict())
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_emsevents() -> None:
    """Show EMS Events"""

    substep("EMS Events")
    print("======================")
    try:
        emsevent = EmsEvent.get_collection()
        for emsevent in EmsEvent.get_collection():
            print("=====")
            pprint.pprint(emsevent.to_dict())
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def show_emsfilter() -> None:
    """Show EMS Filter"""

    substep("EMS Filter")
    print("======================")
    try:
        for emsfilter in EmsFilter.get_collection():
            print("=====")
            print("Filter Name = %s" % emsfilter.name)
            for filterrule in EmsFilterRule.get_collection(emsfilter.name):
                print("Rule:-")
                print("Index:- %s" % filterrule.index)
                try:
                    ruleindex = EmsFilterRule.find(
                        emsfilter.name, index=filterrule.index)
                    pprint.pprint(ruleindex.index)
                    pprint.pprint(ruleindex.message_criteria.name_pattern)
                    pprint.pprint(ruleindex.message_criteria.severities)
                    pprint.pprint(ruleindex.message_criteria.snmp_trap_types)
                    pprint.pprint(ruleindex.type)
                except Exception as e:
                    print("Index cannot be processed")
    except NetAppRestError as error:
        print("Error:- " % error.http_err_response.http_response.text)
        print("Exception caught :" + str(error))


def account_ops():
    """Volume Operations"""
    print()
    print("THE FOLLOWING SCRIPT SHOWS EVENT OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=====================================================================================")
    print()
    emsbool = input(
        "Choose the Event Config Operation[showconfig/showdestination/showevent/showfilter] ")
    if emsbool == 'showevent':
        show_emsevents()
    if emsbool == 'showdestination':
        show_emsdestination()
    if emsbool == 'showconfig':
        show_emsconfig()
    if emsbool == 'showfilter':
        show_emsfilter()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Event Operations using REST API Python Client Library",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    account_ops()


if __name__ == "__main__":
    main()
