# Using Sample Scripts on Lab On Demand

This section will walk you through on how to use the sample scripts found in the example folder in the Lab On Demand Environment.

## Prerequiste

Makes sure that you have the NetApp Support account to log in to the Lab On Demand. 

## Setup

1. Log in to Lab On Demand and from the Library, choose "Exploring the ONTAP REST API v1.2" Lab-On-Demand solution.

2. Log into the "rhel1" machine in the provisioned lab and clone the following respository.

   `git clone https://github.com/NetApp/ontap-rest-python.git`

3. Initialize the environment by running the lab init script.

   `./lod/lod_init.py`

4. Execute scripts from examples/python-client-library and examples/rest-api subfolders.
