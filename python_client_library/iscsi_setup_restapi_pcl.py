#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS ISCSI SETUP USING REST API PCL

usage: iscsi_setup_restapi_pcl.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]

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
from netapp_ontap.resources import Svm, Volume, Node, Aggregate, ExportPolicy, Igroup, Igroup, Lun, LunMap


def get_size(vol_size):
    tmp = int(vol_size) * 1024 * 1024
    return tmp

def show_svm():	
    print()
    print ("Getting SVM Details")
    print ("===================")
    try:
        for svm in Svm.get_collection(fields="uuid"):
            print ("SVM name:-%s ; SVM uuid:-%s " % (svm.name,svm.uuid))
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return	
		
def show_volume(svm_name):	
    print()
    print ("Getting Volume Details")
    print ("===================")
    try:
        for volume in Volume.get_collection(**{"svm.name": svm_name},fields="uuid"):
            print ("Volume name:-%s ; Volume uuid:-%s " % (volume.name,volume.uuid))
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
    return
	
def iscsi_setup():
    print("THE FOLLOWING SCRIPT DEMOSTRATES ISCSI LUN SETUP USING REST API PCL.")
    print("====================================================================")
    print()
    show_svm()
    print()
    svm_name = input("Choose the SVM on which you would like to create a lun : ")
    print("Make sure that ISCSI protocol and LIFs on each nodes are created on the SVM")
    print()
    volbool = input("Would you like to create a new volume (y/n) :-") 
    if volbool == 'y':	
        vol_name = input("Enter the Volume Name:-")
        vol_size = input("Enter the Volume Size (MBs):-")
        aggr_name = input("Enter the aggregate name:-")
 	   
        v_size=get_size(vol_size)
       
        payload1 ={
        "name": vol_name,
        "svm": {"name":svm_name},
        "aggregates": [{"name": aggr_name }],
        "size": v_size
        }
       
        print (payload1) 
        volume = Volume.from_dict(payload1)
        try:
            if(volume.post(poll=True)):
                print ("Volume created  created Successfully")
        except NetAppRestError as e:
            print ("HTTP Error Code is " % e.http_err_response.http_response.text)
            print("Exception caught :" + str(e))
		  
    else:
        print()
        show_volume(svm_name)
        vol_name = input("Choose the volume on which you would like to create the LUN : ")

    print()	
    lun_name = input("Enter the name of the LUN  : ")
    lun_name_ext = "/vol/" + vol_name + "/" + lun_name
    os_type = input("Enter the name of the OS-TYPE  : ")
    lun_size = input("Enter the LUN size in MBs :")
    l_size = get_size(lun_size)
	
    payload2 = {
    "comment": lun_name,
    "location": {
    "logical_unit": lun_name,
    "volume": {
    "name": vol_name
		  }
	  },
    "name": lun_name_ext,
    "os_type": os_type,
    "space": {
		"guarantee": {
		  "requested": bool("")
		},
    "size": l_size
	  },
	  "svm": {
		"name": svm_name
	  }
	}
  
    lunObject = Lun.from_dict(payload2)
	
    try:
        if(lunObject.post(poll=True)):
            print ("LUN created  %s created Successfully" % lunObject.name)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
 
    print()
	
    igroup_name = input("Enter the name of the Igroup that you would like to create  : ")
    initiator_name = input("Enter the name of the Initiator that you would like to add in the InitiatorGroup :")
    os_type2 = 	input("Enter the OS-TYPE :")
	
    payload3 = {
	  "initiators": [
		{
		  "name": initiator_name
		}
	  ],
	  "name": igroup_name,
	  "os_type": os_type2,
	  "svm": {
		"name": svm_name
		 }
	}

    igroupObject = Igroup.from_dict(payload3)
	
    try:
        if(igroupObject.post(poll=True)):
            print ("IGROUP created  %s created Successfully" % igroupObject.name)
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
	   
    payload4 = {
	  "igroup": {
		"name": igroup_name
			  },
	  "lun": {
		"name": lun_name_ext
		
	  },
	  "svm": {
		"name": svm_name
		
	  }
	}   
    
    lunmapObject = LunMap.from_dict(payload4)
    try:
        if(lunmapObject.post(poll=True)):
            print ("Mapping created Successfully" )
    except NetAppRestError as e:
        print ("HTTP Error Code is " % e.http_err_response.http_response.text)
        print("Exception caught :" + str(e))
       
    return


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="THE FOLLOWING SCRIPT SHOWS ISCSI SETUP USING REST API PYTHON CLIENT LIBRARY:-"
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
    iscsi_setup()
    print ("Script Complete")

