#!/bin/bash

################################################################################
#
# Title:	lod_init.sh
#
# Description:	Prepare linux host "rhel1" in LoD lab 
#
# Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
# Licensed under the BSD 3-Clause “New” or Revised” License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# https://opensource.org/licenses/BSD-3-Clause
################################################################################

echo "--> Updating LOD rhel1 system"
yum -y update

echo "--> Installing additional packages"
yum -y install jq

echo "--> Creating links for Python3"
ln -s /usr/local/bin/python3.7 /usr/bin/python3
ln -s /usr/local/bin/pip3.7 /usr/bin/pip3

echo "--> Upgrading Python pip (for both versions)"
pip install --upgrade pip
pip3 install --upgrade pip

echo "--> Installing ONTAP Python client libraries and dependencies"
pip install requests marshmallow texttable
pip install netapp-lib
pip3 install requests marshmallow texttable
pip3 install netapp-lib
pip3 install netapp-ontap
