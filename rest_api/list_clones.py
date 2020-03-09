#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list all clone volumes in a cluster using ONTAP REST API.

usage: python3 list_clones.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
list_clones.py: the following arguments are required: -c/--cluster
"""

import base64
import requests
import time
from subprocess import call
import texttable as tt
import argparse
from getpass import getpass
import logging
requests.packages.urllib3.disable_warnings()

def get_clones(cluster,base64string,headers):
    url = "https://{}/api/storage/volumes/?clone.is_flexclone=true".format(cluster)
    response = requests.get(url, headers=headers,verify=False)
    return response.json()

def disp_vol(cluster,base64string,headers):
    ctr = 0
    tmp = dict(get_clones(cluster,base64string,headers))
    vols = tmp['records']
    tab = tt.Texttable()
    header = ['Clone name']
    tab.header(header)
    tab.set_cols_align(['c'])
    for clonelist in vols:
            ctr = ctr + 1
            vol = clonelist['name']
            row = [vol]
            tab.add_row(row)
            tab.set_cols_align(['c'])
    print ("Number of Cloned Volumes in this cluster:{}".format(ctr))
    cloneoutput = tab.draw()
    print (cloneoutput)


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will list the clones.",
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
    base64string = base64.encodestring(('%s:%s' %(args.api_user,args.api_pass)).encode()).decode().replace('\n', '')
	
    headers = {
    'authorization': "Basic %s" % base64string,
    'content-type': "application/json",
    'accept': "application/json"
    }
	
    disp_vol(args.cluster,base64string,headers)    
