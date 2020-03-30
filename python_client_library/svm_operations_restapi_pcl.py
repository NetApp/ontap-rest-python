#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS SVM OPERATIONS USING REST API PCL

usage: python3 svm_operations_restapi_pcl.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]
									 
Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import argparse
from getpass import getpass
import logging

from netapp_ontap import config,HostConnection, NetAppRestError
from netapp_ontap.resources import Svm, Volume, Node


def show_node():
    print (" Getting Node Details")
    print ("=====================")
	
    try:
        for node in Node.get_collection(fields="uuid"):
            print ("Node name:-%s ; Node uuid:-%s " % (node.name,node.uuid))
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return
    


def show_svm():	
    print ("Getting SVM Details")
    print ("===================")
	
    try:
        for svm in Svm.get_collection(fields="uuid"):
            svm.get()
            print ("SVM name:-%s ; SVM uuid:-%s " % (svm.name,svm.uuid))
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return
	
	
def create_svm():  
    print()
    svmname = input("Enter the name of the SVM: ")
    dataObj = {}
    dataObj['name']=svmname
    dataObj['language']="c.utf_8"
    ipspaceobj={"name":"Default"}
    dataObj['ipspace']=ipspaceobj
    intbool = input("Would you like to configure an Interface (y/n): ")
    if intbool == 'y':
        mgmtlif = input("Enter the name of Management LIF: ")
        ip = input("Enter the IP address: ")
        nm = input("Enter the NetMask: ")
        bd = input("Enter the broadcast-domain: ")
        show_node()
        hn = input("Enter the Home Node: ")
        uuid = input("Enter the UUID: ")
        intjson=[
				{
				"ip":
						{
						"address":ip,
						"netmask":nm
						},
				"location":
						{
						"broadcast_domain":
											{
											"name":bd
											},
						"home_node":{
									"name":hn,
									"uuid":uuid
									}
						},
				"name":mgmtlif,
				"service_policy":"default-data-files"
				}
				]
        dataObj['ip_interfaces']=intjson
    nfsbool = input("Would you like to configure an NFS (y/n): ")
    if nfsbool == 'y':
        nfsjson={"enabled":bool("true")}
        dataObj['nfs']=nfsjson
        print(dataObj)
    cifsbool = input("Would you like to configure an CIFS (y/n): ")
    if cifsbool == 'y':
        fqdn = input("Enter the name of FQDN: ")
        aduser = input("Enter the User: ")
        adpassword = input("Enter the password: ")
        adname = input("Enter the AD Name: ")
        cifsjson={
				"ad_domain":
							{
							"fqdn":fqdn,
							"password":adpassword,
							"user":aduser
							},
				"enabled":bool("true"),
				"name":adname
				}
        dataObj['cifs']=cifsjson
        print(dataObj)
    dnsbool = input("Would you like to configure an DNS (y/n): ")
    if dnsbool == 'y':
        domain = input("Enter the name of Domain: ")
        server = input("Enter the Server: ")
        dnsjson={"domains":[domain],"servers":[server]}
        dataObj['dns']=dnsjson 
        print(dataObj)
	   
    try:
        svm = Svm.from_dict(dataObj)
        if(svm.post(poll=True)):
            print ("SVM  %s created Successfully" % svm.name)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return
	

def patch_svm():
    print()
    show_svm()
    print ("=============================================")
    svmname = input("Enter the name of the SVM that needs to be updated: ")
    svm = Svm.find(name=svmname)
    lanbool = input("Would you like to update language (y/n): ")
    if lanbool == 'y':
        lan = input("Enter the name of language the you would like to update: ")
        svm.language=lan
    namebool = input("Would you like to update the name (y/n): ")
    if namebool == 'y':
        nam = input("Enter the name of SVM: ")
        svm.name=nam
    snapbool = input("Would you like to update an SnapShot Policy (y/n): ")
    if snapbool == 'y':
        snap = input("Enter the name of default snapshot policy that needs to ne updated : ")
        svm.snapshot_policy=snap
    aggrbool = input("Would you like to update the SVM with new Aggregate (y/n): ")
    if aggrbool == 'y':
        aggr = input("Enter the name of aggregates(with commas) that needs to be updated : ")
        svm.aggregates.name=aggr 
	   
    try:   
        if(svm.patch(poll=True)):
            print ("SVM  %s has been updated/patched Successfully" % svm.name)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return

def start_svm():
    print()
    show_svm()
    print()
    print ("=============================================")
    svmname = input("Enter the name of the SVM name that needs to be started: ")
    svm = Svm.find(name=svmname)
    svm.state="running"
	
    try:
        if(svm.patch(poll=True)):
            print ("SVM  %s has been started Successfully" % svm.name)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return

def stop_svm():
    print()
    show_svm()
    print ("=============================================")
    print()
    svmname = input("Enter the name of the SVM name that needs to be stopped: ")
    svm = Svm.find(name=svmname)
    svm.state="stopped"
	
    try:
        if(svm.patch(poll=True)):
            print ("SVM  %s has been stopped Successfully." % svm.name)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return

def delete_svm():
    print()
    show_svm()
    print ("=============================================")
    print()
    svmname = input("Enter the name of the SVM that needs to be deleted: ")
    try:
        svm = Svm.find(name=svmname)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
	
    try:
        if(svm.delete(poll=True)):
            print ("SVM  %s has been deleted Successfully." % svm.name)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return


def svm_ops():
    
    print()
    print("THE FOLLOWING SCRIPT SHOWS SVM OPERATIONS USING REST API PYTHON CLIENT LIBRARY:- ")
    print("=================================================================================")
    print()
    svmget = input("What SVM Operation would you like to do? [show/create/update/start/stop/delete:- ] ")
    if (svmget  == 'show'):
        show_svm()
    if (svmget  == 'create'):
        create_svm()
    if (svmget  == 'update'):
        patch_svm()
    if (svmget  == 'start'):
        start_svm()
    if (svmget  == 'stop'):
        stop_svm()
    if (svmget  == 'delete'):
        delete_svm()
    return
	
def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="THE FOLLOWING SCRIPT SHOWS SVM OPERATIONS USING REST API PCL:-"
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument("-u", "--api_user", default="admin", help="API Username")
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
    args = parse_args()
    config.CONNECTION = HostConnection(
        args.cluster, username=args.api_user, password=args.api_pass, verify=False,
    )

    svm_ops()

