#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to create SVM, Volume and associated Export Policy using ONTAP REST API.

usage: python3 create_svm_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME
                            -sz VOLUME_SIZE -a AGGR_NAME -er
                            EXPORT_POLICY_RULE -en EXPORT_POLICY_NAME
                            [-u API_USER] [-p API_PASS]
create_svm_volume.py:  the following arguments are required: -c/--cluster, -v/--volume_name, -vs/--svm_name, -sz/--volume_size, -a/--aggr_name, -er/--export_policy_rule, -en/--export_policy_name
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


def get_size(volume_size):
    tmp = int(volume_size) * 1024 * 1024
    return tmp

def make_volume(cluster,volume_name,svm_name,volume_size,aggr_name,export_policy_name,base64string,headers):
    v_size=get_size(volume_size)
    print ("Vol Size is :{}".format(v_size))

    url = "https://{}/api/storage/volumes".format(cluster)
    payload = {
    "aggregates.name" : [aggr_name],
    "svm.name": svm_name,
    "name": volume_name,
    "size": v_size,
    "nas": {
    		"export_policy": {
      				"name": export_policy_name
    				 } 
    	   }
    }
    
    response = requests.post(url,headers=headers,json=payload,verify=False)
    time.sleep(5)
    url_text = response.json()
    try:
        job_status = "https://{}/{}".format(cluster,url_text['job']['_links']['self']['href'])
        job_response = requests.get(job_status,headers=headers,verify=False)
        job_status = job_response.json()
        check_vol_job_status(cluster,job_status,headers)
    except:
        print (url_text)
    return


def get_key_svms(cluster,svm_name,base64string,headers):
    tmp = dict(get_svms(cluster,base64string,headers))
    svms = tmp['records']
    for i in svms:
        if i['name'] == svm_name:
            # print i
            return i['uuid']

def get_svms(cluster,base64string,headers):
    url = "https://{}/api/svm/svms".format(cluster)
    r = requests.get(url, headers=headers,verify=False)
    return r.json()


def create_export_policy(cluster,export_policy_name,export_policy_rule,svm_name,base64string,headers):
    url = "https://{}/api/protocols/nfs/export-policies".format(cluster)
    svm_uuid = get_key_svms(cluster,svm_name,base64string,headers)
    payload = {
  	"name": export_policy_name,
  	"rules": [
    			{
                         "clients": [
        			{
          			"match": export_policy_rule
        			}
      				    ],
                          "protocols": [
         				 "any"
      					],
      					"ro_rule": [
        						"any"
      						   ],
      					"rw_rule": [
        						"any"
      						   ]     			
    			}
  		 ],
  	"svm.uuid": svm_uuid
    }
    
    response = requests.post(url,headers=headers,json=payload,verify=False)
    url_text = response.json()

def check_job_status(cluster,job_status,volume_name,svm_name,volume_size,aggr_name,export_policy_rule,export_policy_name,base64string,headers):    
    if (job_status['state'] == "failure"):
        print ("SVM creation failed due to :{}".format(job_status['message']))
        return
    elif(job_status['state'] == "success"):
        print ("SVM created successfully")
        create_export_policy(cluster,export_policy_name,export_policy_rule,svm_name,base64string,headers)
        make_volume(cluster,volume_name,svm_name,volume_size,aggr_name,export_policy_name,base64string,headers)
        return
    else:
        try:
            job_status_url = "https://{}/api/cluster/jobs/{}".format(cluster,job_status['uuid'])
            job_response = requests.get(job_status_url,headers=headers,verify=False)
            job_status = job_response.json()
            time.sleep (5)
            check_job_status(cluster,job_status,volume_name,svm_name,volume_size,aggr_name,export_policy_rule,export_policy_name,base64string,headers)
        except:
            print ("Job errored out. ")

def check_vol_job_status(cluster,job_status,headers):
    if (job_status['state'] == "failure"):
        if (job_status['code'] == 460770):
            print ("Volume Already Exists")
                
        else:
            print ("Volume creation job status :{}".format(job_status['message']))
            return
    elif(job_status['state'] == "success"):
        print ("Volume created successfully")
        return
    else:
        try:
            job_status_url = "https://{}/api/cluster/jobs/{}".format(cluster,job_status['uuid'])
            job_response = requests.get(job_status_url,headers=headers,verify=False)
            job_status = job_response.json()
            time.sleep (5)
            check_vol_job_status(cluster,job_status,headers)
        except:
            print ("The job errored out.")

def make_svm(cluster,volume_name,svm_name,volume_size,aggr_name,export_policy_rule,export_policy_name,base64string,headers):
    url = "https://{}/api/svm/svms".format(cluster)
    payload = {
    "name": svm_name
    }
    response = requests.post(url,headers=headers,json=payload,verify=False)
    time.sleep(5)
    url_text = response.json()    
    try:
        job_status = "https://{}{}".format(cluster,url_text['job']['_links']['self']['href'])
        job_response = requests.get(job_status,headers=headers,verify=False)
        job_status = job_response.json()
        check_job_status(cluster,job_status,volume_name,svm_name,volume_size,aggr_name,export_policy_rule,export_policy_name,base64string,headers)
    except:
        print ("The job errored out.")
        print (url_text)
    return

    
def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will create a SVM, volume and the required export policies.",
    )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
    parser.add_argument(
        "-v", "--volume_name", required=True, help="Name of the volume that needs to be created."
    )
    parser.add_argument(
        "-vs", "--svm_name", required=True, help="SVM that needs to be created."
    )
    parser.add_argument(
        "-sz", "--volume_size", required=True, help="Size of the Volume."
    )
    parser.add_argument(
        "-a", "--aggr_name", required=True, help="Aggregate Name."
    )
    parser.add_argument(
        "-er", "--export_policy_rule", required=True, help="Export Policy Rule."
    )
    parser.add_argument(
        "-en", "--export_policy_name", required=True, help="Export Policy Name"
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
	
    make_svm(args.cluster,args.volume_name,args.svm_name,args.volume_size,args.aggr_name,args.export_policy_rule,args.export_policy_name,base64string,headers)    
