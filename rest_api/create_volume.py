#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to create Volume using ONTAP REST API.

usage:python3 create_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a
                        AGGR_NAME -sz VOLUME_SIZE [-u API_USER] [-p API_PASS]
create_volume.py: the following arguments are required: -c/--cluster, -v/--volume_name, -vs/--svm_name, -a/--aggr_name, -sz/--volume_size

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""


import time
import base64
import argparse
import json
import requests 
import argparse
from getpass import getpass
import logging
requests.packages.urllib3.disable_warnings()

def get_svms(cluster,base64string,headers):
    url = "https://{}/api/svm/svms".format(cluster)
    response = requests.get(url, headers=headers,verify=False)
    return response.json()


def get_key_svms(cluster,svm_name,base64string,headers):
    tmp = dict(get_svms(cluster,base64string,headers))
    svms = tmp['records']
    for i in svms:
        if i['name'] == svm_name:
            return i['uuid']

    
def get_vols():
    url = "https://{}/api/storage/volumes/".format(api)
    response = requests.get(url, headers=headers,verify=False)
    return response.json()
      
def get_size(volume_size):
    tmp = int(volume_size) * 1024 * 1024
    return tmp


def check_job_status(cluster,job_status,base64string,headers):
    if (job_status['state'] == "failure"):
        print ("Volume creation failed due to :{}".format(job_status['message']))
        return
    elif(job_status['state'] == "success"):
        print ("Volume created successfully")
        return
    else:
        job_status_url = "https://{}/api/cluster/jobs/{}".format(cluster,job_status['uuid'])
        job_response = requests.get(job_status_url,headers=headers,verify=False)
        job_status = job_response.json()
        check_job_status(cluster,job_status,base64string,headers)

def make_volume(cluster,volume_name,svm_name,aggr_name,volume_size,base64string,headers):
    svm_key=get_key_svms(cluster,svm_name,base64string,headers)
    v_size=get_size(volume_size)
    print ("Vol Size is :{}".format(v_size))

    url = "https://{}/api/storage/volumes".format(cluster) 
    payload = {
    "aggregates.name" : [aggr_name],
    "svm.name": svm_name,
    "name": volume_name,
    "size": v_size
    }
 
    response = requests.post(url,headers=headers,json=payload,verify=False)
    url_text = response.json()
    job_status = "https://{}/{}".format(cluster,url_text['job']['_links']['self']['href'])
    job_response = requests.get(job_status,headers=headers,verify=False)
    job_status = job_response.json()
    check_job_status(cluster,job_status,base64string,headers)
    return


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
    description="This script will create an ONTAP volume in an SVM",
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-v", "--volume_name", required=True, help="Name of the volume that needs to be created."
    )
    parser.add_argument(
        "-vs", "--svm_name", required=True, help="svm name"
    )
    parser.add_argument(
        "-a", "--aggr_name", required=True, help="Aggregate Name"
    )
    parser.add_argument(
        "-sz", "--volume_size", required=True, help="Volume Size"
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
    base64string = base64.encodestring(('%s:%s' %(args.api_user,args.api_pass)).encode()).decode().replace('\n', '')
	
    headers = {
    'authorization': "Basic %s" % base64string,
    'content-type': "application/json",
    'accept': "application/json"
    }
	
    make_volume(args.cluster,args.volume_name,args.svm_name,args.aggr_name,args.volume_size,base64string,headers)    


