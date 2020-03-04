#! /usr/bin/env python3

"""
ONTAP REST API Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies.  This script is not officially supported as a
standard NetApp product.

Purpose: Script to list all the aggregates in a cluster using ONTAP REST API.

usage:python3 list_aggregates.py [-h] -c CLUSTER [-u API_USER] [-p API_PASS]
list_aggregates.py:  the following arguments are required: -c/--cluster
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


def get_aggr(cluster,base64string,headers):
    url = "https://{}/api/storage/aggregates".format(cluster)
    response = requests.get(url, headers=headers,verify=False)
    return response.json()


def disp_aggr(cluster,base64string,headers):
    ctr = 0
    tmp = dict(get_aggr(cluster,base64string,headers))
    aggr = tmp['records']
    #print aggr
    tab = tt.Texttable()
    header = ['Aggregate name']
    tab.header(header)
    tab.set_cols_align(['c'])
    for i in aggr:
        ctr = ctr + 1
        ag = i['name']
	#si = i['size_avail']
        #si = si/1024/1024/1024
        row = [ag]
        tab.add_row(row)
        tab.set_cols_align(['c'])
    print ("Number of Aggregates for the NetApp cluster:{}".format(ctr))
    s = tab.draw()
    print (s)

	
def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
    description="This script will list aggregates.",
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
	
    disp_aggr(args.cluster,base64string,headers)
    


