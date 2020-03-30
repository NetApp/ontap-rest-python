#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API

usage: python3 volume_operations_restapi_api.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import sys
import time
import base64
import argparse
import requests
import json
import requests
import logging
from getpass import getpass
requests.packages.urllib3.disable_warnings()


def get_size(vol_size):
    """ convert to bytes"""
    tmp = int(vol_size) * 1024 * 1024
    return tmp


def get_snapshots(cluster, base64string, headers, vol_uuid):
    """ get snapshots json"""
    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
    try:
        job_response = requests.get(
            snap_api_url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    return r.json()


def get_key_snapshot(snapshot_name, vol_uuid):
    print()
    tmp = dict(get_snapshots(cluster, base64string, headers, vol_uuid))
    snap = tmp['records']
    print()
    print("The UUID of the Snapshot is ")
    for i in snap:
        if i['name'] == snapshot_name:
            print(i['uuid'])
            return i['uuid']


def get_volumes(cluster, base64string, headers):
    """ get volumes json"""
    url = "https://{}/api/storage/volumes/".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    return r.json()


def get_key_volumes(vol_name, cluster, base64string, headers):
    """ get volume keys"""
    print()
    tmp = dict(get_volumes(cluster, base64string, headers))
    vols = tmp['records']
    print()
    print("The UUID of the Volume is ")
    for i in vols:
        if i['name'] == vol_name:
            print(i['uuid'])
            return i['uuid']


def get_svms(cluster, base64string, headers):
    """ get the svm json"""
    url = "https://{}/api/svm/svms".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    return r.json()


def get_key_svms(svm_name, cluster, base64string, headers):
    """ get svm key"""
    tmp = dict(get_svms(cluster, base64string, headers))
    svms = tmp['records']
    print("The UUID of the SVM is ")
    for i in svms:
        if (i['name']) == svm_name:
            print(i['uuid'])
            return i['uuid']


def show_svm(cluster, base64string, headers):
    """ List the svm"""
    url = "https://{}/api/svm/svms".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tmp = dict(r.json())
    svms = tmp['records']
    print()
    print(" List of SVMs:- ")
    print("================")
    for i in svms:
        print(i['name'])
    return r.json()


def show_volume(cluster, base64string, headers):
    """ list the volumes"""
    print("The List of SVMs")
    show_svm(cluster, base64string, headers)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    print("Getting Volume Details")
    print("======================")
    url = "https://{}/api/storage/volumes/?svm.name={}".format(
        cluster, svm_name)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tmp = dict(r.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print("Volume Name :- %s; Volume UUID :- %s" % (i['name'], i['uuid']))
    return


def show_snapshot(cluster, base64string, headers):
    """ list snapshots"""
    print("The List of Volumes")
    show_volume(cluster, base64string, headers)
    print()
    vol_name = input(
        "Enter the Volume from which the Snapshot need to be listed:-")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
    print()
    print("Getting Snapshot Details")
    print("======================")
    snap_api_url = "https://{}/api/storage/volumes/{}/snapshots".format(
        cluster, vol_uuid)
    try:
        r = requests.get(snap_api_url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = r.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    tmp = dict(r.json())
    svms = tmp['records']
    print()
    for i in svms:
        print(i['name'])
    return r.json()


def show_aggregate(cluster, base64string, headers):
    """ list aggregates"""
    url = "https://{}/api/storage/aggregates".format(cluster)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    tmp = dict(r.json())
    aggr = tmp['records']
    print()
    print("List of Aggregates:- ")
    print("=====================")
    for i in aggr:
        print(i['name'])
    return


def check_job_status(job_status, headers, cluster):
    """ check job status"""
    if (job_status['state'] == "failure"):
        if (job_status['code'] == 460770):
            print("SVM Already Exists")
        else:
            print("Operation failed due to :{}".format(job_status['message']))
            return
    elif(job_status['state'] == "success"):
        print("Operation completed successfully.")
        return
    else:
        job_status_url = "https://{}/api/cluster/jobs/{}".format(
            cluster, job_status['uuid'])
        try:
            job_response = requests.get(
                job_status_url, headers=headers, verify=False)
        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print(err)
            sys.exit(1)
        job_status = job_response.json()
        time.sleep(5)
        check_job_status(job_status, headers, cluster)
    return


def delete_volume(cluster, base64string, headers):
    """ delete the volume"""
    print("=============================================")
    print()
    show_volume(cluster, base64string, headers)
    print()
    volname = input("Enter the name of the volume that needs to be Deleted:- ")
    vol_uuid = get_key_volumes(volname, cluster, base64string, headers)
    dataObj = {}
    urlpath = "https://{}/api/storage/volumes/" + vol_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.delete(
            url, headers=headers, json=dataObj, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(job_status, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers, cluster)
    return


def create_volume(cluster, base64string, headers):
    """ create volume"""
    print()
    show_svm(cluster, base64string, headers)
    print()
    svmname = input(
        "Enter the name of the SVM on which the volume needs to be created:- ")
    dataObj = {}
    tmp1 = {"name": svmname}
    dataObj['svm'] = tmp1
    print()
    show_aggregate(cluster, base64string, headers)
    print()
    aggrname = input(
        "Enter the name of the Aggregate on which the volume needs to be created:- ")
    tmp2 = [{"name": aggrname}]
    dataObj['aggregates'] = tmp2
    print()
    volname = input("Enter the name of the Volume:- ")
    dataObj['name'] = volname
    print()
    vol_size = input("Enter the size of the Volume in MB:- ")
    tmp3 = get_size(vol_size)
    dataObj['size'] = tmp3
    print()
    voltype = input("Enter the Volume Type[rw/dp]:- ")
    dataObj['type'] = voltype
    print()
    styletype = input("Enter the Volume Style Type[flexvol]:- ")
    dataObj['style'] = styletype
    print()
    autosize = input("Would you like to enable Autosize (y/n): ")
    if autosize == 'y':
        print("Enter the following Details")
        grow_threshold = input("grow_threshold?:- ")
        maximum = input("maximum?:- ")
        minimum = input("minimum?:- ")
        mode = input("mode?:- ")
        shrink_threshold = input("shrink_threshold?:- ")
        autosizejson = {
            "grow_threshold": grow_threshold,
            "maximum": maximum,
            "minimum": minimum,
            "mode": mode,
            "shrink_threshold": shrink_threshold}
        dataObj['autosize'] = autosizejson
    print()
    efficiency = input("Would you like to enable Efficiency (y/n): ")
    if efficiency == 'y':
        print("Enter the following Details")
        compaction = input("compaction?:- ")
        compression = input("compression?:- ")
        cross_volume_dedupe = input("cross_volume_dedupe?:- ")
        dedupe = input("dedupe?:- ")
        policy_name_e = input("Efficiency Policy Name?:- ")
        efficiencyjson = {
            "compaction": compaction,
            "compression": compression,
            "cross_volume_dedupe": cross_volume_dedupe,
            "dedupe": dedupe,
            "policy": {
                "name": policy_name_e}}
        dataObj['efficiency'] = efficiencyjson
    print()
    encryption = input("Would you like to enable Encryption (y/n): ")
    if encryption == 'y':
        print("Enter the following Details")
        enabled_encry = input("Enable Encryption ?:- ")
        encryptionjson = {"enabled": bool(enabled_encry), "status": {}}
        dataObj['encryption'] = encryptionjson
    print()
    files = input("Would you like to enable Max File Count (y/n): ")
    if files == 'y':
        print("Enter the following Details")
        maximum_files = input("Max File Count?:- ")
        filesjson = {"maximum": maximum_files}
        dataObj['files'] = filesjson
    print()
    nas = input("Would you like to enable NAS parameters (y/n): ")
    if nas == 'y':
        print("Enter the following Details")
        export_policy_name = input("export_policy_name?:- ")
        path = input("path?:- ")
        security_style = input("security_style?:- ")
        unix_permissions = input("unix_permissions?:- ")
        nasjson = {
            "export_policy": {
                "name": export_policy_name},
            "path": path,
            "security_style": security_style,
            "unix_permissions": unix_permissions}
        dataObj['efficiency'] = nasjson
    print()
    qos = input("Would you like to enable QoS (y/n): ")
    if qos == 'y':
        print("Enter the following Details")
        max_throughput_iops = input("max_throughput_iops?:- ")
        max_throughput_mbps = input("max_throughput_mbps?:- ")
        min_throughput_iops = input("min_throughput_iops?:- ")
        qosname = input("qosname?:- ")
        qosjson = {
            "policy": {
                "max_throughput_iops": max_throughput_iops,
                "max_throughput_mbps": max_throughput_mbps,
                "min_throughput_iops": min_throughput_iops,
                "name": qosname}}
        dataObj['qos'] = qosjson
    print()
    quota = input("Would you like to enable Quota (y/n): ")
    if quota == 'y':
        print("Enter the following Details")
        enable_quota = input("enable_quota?:- ")
        quotajson = {"enabled": bool(enable_quota)}
        dataObj['quota'] = quotajson
    print(dataObj)
    url = "https://{}/api/storage/volumes".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers,
            json=dataObj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(job_status, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers, cluster)
    return


def patch_volume(cluster, base64string, headers):
    """ update a volume"""
    print("=============================================")
    print()
    show_volume(cluster, base64string, headers)
    print()
    volname = input(
        "Enter the name of the volume that needs to be modified:- ")
    dataObj = {}
    dataObj['name'] = volname
    print()
    nambool = input("Would you like to change the volume name (y/n):- ")
    if nambool == 'y':
        nam = input("Enter the new name of the Volume (y/n): ")
        dataObj['name'] = nam
    print()
    sizebool = input("Would you like to change the volume size (y/n):- ")
    if sizebool == 'y':
        vol_size = input("Enter the new size of the Volume: ")
        vol_size_format = get_size(vol_size)
        dataObj['size'] = vol_size_format
    autosizebool = input("Would you like to change autosize options (y/n):- ")
    if autosizebool == 'y':
        print("Enter the following Details")
        grow_threshold = input("grow_threshold?:- ")
        maximum = input("maximum?:- ")
        minimum = input("minimum?:- ")
        mode = input("mode?:- ")
        shrink_threshold = input("shrink_threshold?:- ")
        autosizejson = {
            "grow_threshold": grow_threshold,
            "maximum": maximum,
            "minimum": minimum,
            "mode": mode,
            "shrink_threshold": shrink_threshold}
        dataObj['autosize'] = autosizejson
    print()
    efficiency = input("Would you like to enable Efficiency (y/n): ")
    if efficiency == 'y':
        print("Enter the following Details")
        compaction = input("compaction?:- ")
        compression = input("compression?:- ")
        cross_volume_dedupe = input("cross_volume_dedupe?:- ")
        dedupe = input("dedupe?:- ")
        policy_name_e = input("Efficiency Policy Name?:- ")
        efficiencyjson = {
            "compaction": compaction,
            "compression": compression,
            "cross_volume_dedupe": cross_volume_dedupe,
            "dedupe": dedupe,
            "policy": {
                "name": policy_name_e}}
        dataObj['efficiency'] = efficiencyjson
    print()
    encryption = input("Would you like to enable Encryption (y/n): ")
    if encryption == 'y':
        print("Enter the following Details")
        enabled_encry = input("Enable Encryption ?:- ")
        encryptionjson = {"enabled": bool(enabled_encry), "status": {}}
        dataObj['encryption'] = encryptionjson
    print()
    files = input("Would you like to enable Max File Count (y/n): ")
    if files == 'y':
        print("Enter the following Details")
        maximum_files = input("Max File Count?:- ")
        filesjson = {"maximum": maximum_files}
        dataObj['files'] = filesjson
    print()
    nas = input("Would you like to enable NAS parameters (y/n): ")
    if nas == 'y':
        print("Enter the following Details")
        export_policy_name = input("export_policy_name?:- ")
        path = input("path?:- ")
        security_style = input("security_style?:- ")
        unix_permissions = input("unix_permissions?:- ")
        nasjson = {
            "export_policy": {
                "name": export_policy_name},
            "path": path,
            "security_style": security_style,
            "unix_permissions": unix_permissions}
        dataObj['efficiency'] = nasjson
    print()
    qos = input("Would you like to enable QoS (y/n): ")
    if qos == 'y':
        print("Enter the following Details")
        max_throughput_iops = input("max_throughput_iops?:- ")
        max_throughput_mbps = input("max_throughput_mbps?:- ")
        min_throughput_iops = input("min_throughput_iops?:- ")
        qosname = input("qosname?:- ")
        qosjson = {
            "policy": {
                "max_throughput_iops": max_throughput_iops,
                "max_throughput_mbps": max_throughput_mbps,
                "min_throughput_iops": min_throughput_iops,
                "name": qosname}}
        dataObj['qos'] = qosjson
    print()
    quota = input("Would you like to enable Quota (y/n): ")
    if quota == 'y':
        print("Enter the following Details")
        enable_quota = input("enable_quota?:- ")
        quotajson = {"enabled": bool(enable_quota)}
        dataObj['quota'] = quotajson

    vol_uuid = get_key_volumes(volname, cluster, base64string, headers)
    print()
    urlpath = "https://{}/api/storage/volumes/" + vol_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.patch(
            url, headers=headers, json=dataObj, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(job_status, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers, cluster)
    return


def clone_volume(cluster, base64string, headers):
    """ Clone a volume"""
    print("=============================================")
    print()
    show_volume(cluster, base64string, headers)
    print()
    vol_name = input("Enter the name of the volume that needs to be Cloned:- ")
    vol_uuid = get_key_volumes(vol_name, cluster, base64string, headers)
    print()
    show_svm(cluster, base64string, headers)
    print()
    dataObj = {}
    clone_name = input("Enter the name of the clone:- ")
    svm_name = input(
        "Enter the name of the SVM the parent volume belongs to:- ")
    svm_uuid = get_key_svms(svm_name, cluster, base64string, headers)
    tmp = {'uuid': svm_uuid}
    dataObj['svm'] = tmp
    dataObj['name'] = clone_name
    clone_volume_json = {
        "is_flexclone": bool("true"), "parent_svm": {
            "name": svm_name, "uuid": svm_uuid}, "parent_volume": {
            "name": vol_name, "uuid": vol_uuid}}
    dataObj['clone'] = clone_volume_json
    clonesnapshot = input("Would you like to Clone from Snapshot (y/n): ")
    if clonesnapshot == 'y':
        snapshot_name = input(
            "Enter the name of the snapshot that needs to be Cloned:- ")
        snapshot_uuid = get_key_snapshot(snapshot_name, vol_uuid)
        clone_snapshot_json = {
            "is_flexclone": bool(true), "parent_snapshot": {
                "name": snapshot_name, "uuid": snapshot_uuid}, "parent_svm": {
                "name": svmname, "uuid": svm_uuid}, "parent_volume": {
                "name": vol_name, "uuid": vol_uuid}}
        dataObj['clone'] = clone_snapshot_json
    print(dataObj)
    url = "https://{}/api/storage/volumes".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers,
            json=dataObj,
            verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = "https://{}{}".format(cluster,
                                       url_text['job']['_links']['self']['href'])
    try:
        job_response = requests.get(job_status, headers=headers, verify=False)
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    url_text = job_response.json()
    if 'error' in url_text:
        print(url_text)
        sys.exit(1)
    job_status = job_response.json()
    check_job_status(job_status, headers, cluster)
    return


def volume_ops(cluster, base64string, headers):
    print()
    print("THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API:- ")
    print("============================================================")
    print()
    volumebool = input(
        "What Volume Operation would you like to do? [show/create/update/delete/clone] ")
    if volumebool == 'show':
        show_volume(cluster, base64string, headers)
    if volumebool == 'create':
        create_volume(cluster, base64string, headers)
    if volumebool == 'update':
        patch_volume(cluster, base64string, headers)
    if volumebool == 'delete':
        delete_volume(cluster, base64string, headers)
    if volumebool == 'clone':
        clone_volume(cluster, base64string, headers)
    return


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(
        description="THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API.", )
    parser.add_argument(
        "-c", "--cluster", required=True, help="API server IP:port details"
    )
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
    args = parse_args()
    base64string = base64.encodestring(
        ('%s:%s' %
         (args.api_user, args.api_pass)).encode()).decode().replace(
        '\n', '')

    headers = {
        'authorization': "Basic %s" % base64string,
        'content-type': "application/json",
        'accept': "application/json"
    }

    volume_ops(args.cluster, base64string, headers)

    print("Script Complete")
