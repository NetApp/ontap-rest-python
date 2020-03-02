#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts
          
This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to create a clone.

usage: create_clone.py [-h] -c CLUSTER -v VOLUME_NAME -vn VSERVER_NAME -sn
                       SNAPSHOT_NAME -cn CLONE_NAME -a AGGR_NAME [-u API_USER]
                       [-p API_PASS]
create_clone.py: the following arguments are required: -c/--cluster,
 -v/--volume_name, -vn/--vserver_name, -sn/--snapshot_name, -cn/--clone_name,
 -a/--aggr_name
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

def get_key_vol(cluster,volume_name,base64string,headers):
    tmp = dict(get_vols(cluster,base64string,headers))
    vols = tmp['records']
    for i in vols:
        if i['name'] == volume_name:
            return i['uuid']

def get_vols(cluster,base64string,headers):
    url = "https://{}/api/storage/volumes/".format(cluster)
    r = requests.get(url, headers=headers,verify=False)
    return r.json()
      

def check_job_status(cluster,job_status,base64string,headers):    
    if (job_status['state'] == "failure"):
        print ("Clone creation failed due to :{}".format(job_status['message']))
        return
    elif(job_status['state'] == "success"):
        print ("Clone created successfully")
        return
    else:
        print ("Clone creation in process...")
        time.sleep(2)
        url_text='/api/cluster/jobs/'+ job_status['uuid']
        job_status = "https://{}/{}".format(cluster,url_text)
        job_response = requests.get(job_status,headers=headers,verify=False)
        job_status = job_response.json()
        check_job_status(job_status,base64string,headers)

def make_clone(cluster,volume_name,vserver_name,snapshot_name,aggr_name,clone_name,base64string,headers):
    vol_key=get_key_vol(cluster,vserver_name,base64string,headers)
    url = "https://{}/api/storage/volumes".format(cluster) 
    payload = {
    "svm.name": vserver_name,
    "clone.is_flexclone": "true",
    "clone.parent_snapshot.name": snapshot_name,
    "clone.parent_volume.name": volume_name,
    "name": clone_name
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
        description="This script will create a clone of the volume in an SVM.",
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-v", "--volume_name", required=True, help="Volume from which clone need to be created."
    )
    parser.add_argument(
        "-vn", "--vserver_name", required=True, help="SVM to create the Clone from"
    )
    parser.add_argument(
        "-sn", "--snapshot_name", required=True, help="Snapshot name"
    )
    parser.add_argument(
        "-cn", "--clone_name", required=True, help="Clone name"
    )
    parser.add_argument(
        "-a", "--aggr_name", required=True, help="Aggregate on which clone need to be created."
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
	
    make_clone(args.cluster,args.volume_name,args.vserver_name,args.snapshot_name,args.aggr_name,args.clone_name,base64string,headers)    

