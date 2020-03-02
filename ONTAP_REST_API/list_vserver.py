#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list SVMs.

Usage: list_vserver.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
list_vserver.py: the following arguments are required: -c/--cluster
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


def get_vservers(cluster,base64string,headers):
    url = "https://{}/api/svm/svms".format(cluster)
    response = requests.get(url, headers=headers,verify=False)
    return response.json()



def disp_vservers(cluster,base64string,headers):
    ctr = 0
    tmp = dict(get_vservers(cluster,base64string,headers))
    vservers = tmp['records']
    tab = tt.Texttable()
    header = ['Vserver name']
    tab.header(header)
    tab.set_cols_align(['c'])
    for i in vservers:
        ctr = ctr + 1
        cl = i['name']
        row = [cl]
        tab.add_row(row)
        tab.set_cols_align(['c'])
    print ("Number of Storage Tenants on the NetApp cluster :{}".format(ctr))
    s = tab.draw()
    print (s)


	
def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="This script will list SVMs",
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
	
    disp_vservers(args.cluster,base64string,headers) 


