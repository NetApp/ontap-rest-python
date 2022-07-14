#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate NetApp technologies. This
script is not officially supported as a standard NetApp product.

Purpose: THE FOLLOWING SCRIPT SHOWS VOLUME OPERATIONS USING REST API

usage: python3 volume_operations.py [-h] -c CLUSTER [-u API_USER]
                                     [-p API_PASS]

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""
import sys
import requests
import urllib3 as ur
from utils import Argument, parse_args, setup_logging, setup_connection, get_size
from utils import get_key_volumes, get_key_svms, show_svm, show_volume, show_snapshot
from utils import get_key_snapshot, show_aggregate, check_job_status
ur.disable_warnings()


def list_volume(cluster: str, headers_inc: str):
    """ List the volumes"""
    print("The List of SVMs")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    print("Getting Volume Details")
    print("======================")
    url = "https://{}/api/storage/volumes/?svm.name={}".format(
        cluster, svm_name)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
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
    tmp = dict(response.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print("Volume Name :- %s; Volume UUID :- %s" % (i['name'], i['uuid']))

def space_used_snap_vol(cluster: str, headers_inc: str, space_per_snap: str):
    """Filter volumes by % of snapshot reserve size that has been used"""
    print("\n\nFilter volumes by Percentage of snapshot reserve size that has been used")
    print("========================================================================")
    url = "https://{}/api/storage/volumes/?space.snapshot.space_used_percent={}".format(
        cluster, space_per_snap)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
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
    tmp = dict(response.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print("Volume Name :- %s \nVolume UUID :- %s\n\n" % (i['name'], i['uuid']))


def space_avail_vol_per(cluster: str, headers_inc: str, space_per: str):
    """Filter volumes by % of snapshot reserve size that has been used"""
    print("\n\nFilter volumes by the space available, as a percent.")
    print("========================================================================")
    url = "https://{}/api/storage/volumes/?space.available_percent={}".format(
        cluster, space_per)
    try:
        response = requests.get(url, headers=headers_inc, verify=False)
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
    tmp = dict(response.json())
    svms = tmp['records']
    print()
    print("List of Volumes :- ")
    print("===================")
    for i in svms:
        print("Volume Name :- %s \nVolume UUID :- %s\n\n" % (i['name'], i['uuid']))        

def delete_volume(cluster: str, headers_inc: str):
    """ Delete the volume"""
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the name of the volume that needs to be Deleted:- ")
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    dataobj = {}
    urlpath = "https://{}/api/storage/volumes/" + vol_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.delete(
            url, headers=headers_inc, json=dataobj, verify=False)
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
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
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
    check_job_status(job_status, headers_inc, cluster)


def create_volume(cluster: str, headers_inc: str):
    """Create volume"""
    print()
    show_svm(cluster, headers_inc)
    print()
    svmname = input(
        "Enter the name of the SVM on which the volume needs to be created:- ")
    dataobj = {}
    tmp1 = {"name": svmname}
    dataobj['svm'] = tmp1
    print()
    show_aggregate(cluster, headers_inc)
    print()
    aggrname = input(
        "Enter the name of the Aggregate on which the volume needs to be created:- ")
    tmp2 = [{"name": aggrname}]
    dataobj['aggregates'] = tmp2
    print()
    volname = input("Enter the name of the Volume:- ")
    dataobj['name'] = volname
    print()
    vol_size = input("Enter the size of the Volume in MB:- ")
    tmp3 = get_size(vol_size)
    dataobj['size'] = tmp3
    print()
    voltype = input("Enter the Volume Type[rw/dp]:- ")
    dataobj['type'] = voltype
    print()
    styletype = input("Enter the Volume Style Type[flexvol]:- ")
    dataobj['style'] = styletype
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
        dataobj['autosize'] = autosizejson
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
        dataobj['efficiency'] = efficiencyjson
    print()
    encryption = input("Would you like to enable Encryption (y/n): ")
    if encryption == 'y':
        print("Enter the following Details")
        enabled_encry = input("Enable Encryption ?:- ")
        encryptionjson = {"enabled": bool(enabled_encry), "status": {}}
        dataobj['encryption'] = encryptionjson
    print()
    files = input("Would you like to enable Max File Count (y/n): ")
    if files == 'y':
        print("Enter the following Details")
        maximum_files = input("Max File Count?:- ")
        filesjson = {"maximum": maximum_files}
        dataobj['files'] = filesjson
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
        dataobj['efficiency'] = nasjson
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
        dataobj['qos'] = qosjson
    print()
    quota = input("Would you like to enable Quota (y/n): ")
    if quota == 'y':
        print("Enter the following Details")
        enable_quota = input("enable_quota?:- ")
        quotajson = {"enabled": bool(enable_quota)}
        dataobj['quota'] = quotajson
    print(dataobj)
    url = "https://{}/api/storage/volumes".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
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
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
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
    check_job_status(job_status, headers_inc, cluster)


def patch_volume(cluster: str, headers_inc: str):
    """ Update a volume"""
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volname = input(
        "Enter the name of the volume that needs to be modified:- ")
    dataobj = {}
    dataobj['name'] = volname
    print()
    nambool = input("Would you like to change the volume name (y/n):- ")
    if nambool == 'y':
        nam = input("Enter the new name of the Volume: ")
        dataobj['name'] = nam
    print()
    sizebool = input("Would you like to change the volume size (y/n):- ")
    if sizebool == 'y':
        vol_size = input("Enter the new size of the Volume: ")
        vol_size_format = get_size(vol_size)
        dataobj['size'] = vol_size_format
    print()
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
        dataobj['autosize'] = autosizejson
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
        dataobj['efficiency'] = efficiencyjson
    print()
    encryption = input("Would you like to enable Encryption (y/n): ")
    if encryption == 'y':
        print("Enter the following Details")
        enabled_encry = input("Enable Encryption ?:- ")
        encryptionjson = {"enabled": bool(enabled_encry), "status": {}}
        dataobj['encryption'] = encryptionjson
    print()
    files = input("Would you like to enable Max File Count (y/n): ")
    if files == 'y':
        print("Enter the following Details")
        maximum_files = input("Max File Count?:- ")
        filesjson = {"maximum": maximum_files}
        dataobj['files'] = filesjson
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
        dataobj['efficiency'] = nasjson
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
        dataobj['qos'] = qosjson
    print()
    quota = input("Would you like to enable Quota (y/n): ")
    if quota == 'y':
        print("Enter the following Details")
        enable_quota = input("enable_quota?:- ")
        quotajson = {"enabled": bool(enable_quota)}
        dataobj['quota'] = quotajson

    vol_uuid = get_key_volumes(svm_name, volname, cluster, headers_inc)
    print()
    urlpath = "https://{}/api/storage/volumes/" + vol_uuid
    url = urlpath.format(cluster)
    try:
        response = requests.patch(
            url, headers=headers_inc, json=dataobj, verify=False)
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
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
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
    check_job_status(job_status, headers_inc, cluster)


def clone_volume(cluster: str, headers_inc: str):
    """ Clone a volume"""
    print("=============================================")
    show_svm(cluster, headers_inc)
    print()
    svm_name = input(
        "Enter the SVM from which the Volumes need to be listed:-")
    print()
    show_volume(cluster, headers_inc, svm_name)
    print()
    volume_name = input(
        "Enter the name of the volume that needs to be Cloned:- ")
    vol_uuid = get_key_volumes(svm_name, volume_name, cluster, headers_inc)
    print()
    clone_name = input("Enter the name of the clone:- ")
    dataobj = {}
    svm_uuid = get_key_svms(svm_name, cluster, headers_inc)
    tmp = {'uuid': svm_uuid}
    dataobj['svm'] = tmp
    dataobj['name'] = clone_name
    clone_volume_json = {
        "is_flexclone": bool("true"), "parent_svm": {
            "name": svm_name, "uuid": svm_uuid}, "parent_volume": {
                "name": volume_name, "uuid": vol_uuid}}
    dataobj['clone'] = clone_volume_json
    clonesnapshot = input("Would you like to Clone from Snapshot (y/n): ")
    if clonesnapshot == 'y':
        show_snapshot(svm_name, volume_name, cluster, headers_inc)
        snapshot_name = input(
            "Enter the name of the snapshot that needs to be Cloned:- ")
        snapshot_uuid = get_key_snapshot(
            svm_name, volume_name, snapshot_name, cluster, headers_inc)
        clone_snapshot_json = {
            "is_flexclone": bool("true"), "parent_snapshot": {
                "name": snapshot_name, "uuid": snapshot_uuid}, "parent_svm": {
                    "name": svm_name, "uuid": svm_uuid}, "parent_volume": {
                        "name": volume_name, "uuid": vol_uuid}}
        dataobj['clone'] = clone_snapshot_json
    print(dataobj)
    url = "https://{}/api/storage/volumes".format(cluster)
    try:
        response = requests.post(
            url,
            headers=headers_inc,
            json=dataobj,
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
        job_response = requests.get(
            job_status, headers=headers_inc, verify=False)
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
    check_job_status(job_status, headers_inc, cluster)


def volume_ops(cluster: str, headers_inc: str):
    """Volume Operation"""
    print()
    print("Demostrates the Volume Operations:- ")
    print("====================================")
    print()
    print("What Volume Operation would you like to do? [list/create/update/delete/clone/] ")
    print("Filter volumes by: \n 1.  Percentage of snapshot reserve size that has been used : \n 2.  Space available, as a percent")
    volumebool = input ("\n\nenter an option: ")    
    if volumebool == 'list':
        list_volume(cluster, headers_inc)
    if volumebool == 'create':
        create_volume(cluster, headers_inc)
    if volumebool == 'update':
        patch_volume(cluster, headers_inc)
    if volumebool == 'delete':
        delete_volume(cluster, headers_inc)
    if volumebool == 'clone':
        clone_volume(cluster, headers_inc)
    if volumebool == '1':
        space_per_snap = input("\n\nEnter the Percentage of snapshot reserve size that has been used: ")
        space_used_snap_vol(cluster, headers_inc, space_per_snap)
    if volumebool == '2':
        space_per = input("\n\nEnter the required filter space available, as a percent: ")
        space_avail_vol_per(cluster, headers_inc, space_per)    

def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details")]
    args = parse_args(
        "Demonstrates Volume Operations using REST API.", arguments,
    )
    setup_logging()
    headers = setup_connection(args.api_user, args.api_pass)

    volume_ops(args.cluster, headers)


if __name__ == "__main__":
    main()
