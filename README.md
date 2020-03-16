# ONTAP-REST-API

Sample scripts for illustrating the use of ONTAP REST APIs and  ONTAP REST API Python Client Libraries.

## Using ONTAP REST API


NetApp® ONTAP® version 9.6 and above, adds support for an expanded RESTful API. In comparison to the ONTAPI® application, the ONTAP REST APIs offer a vastly simplified workflow-driven user experience, enabling you to perform multiple operations on a given storage object with a single API. RESTful APIs are the industry standard, and as enterprises are standardizing on RESTful APIs, we have a tremendous opportunity to make inroads into new segments.

The ONTAP_REST_API folder contains samples scripts to illustrate how ONTAP REST APIs can be used.


Deploy the scripts with the appropriate parameters.

eg:-

python3 create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a
                            AGGR_NAME -sz VOLUME_SIZE [-u API_USER]
                            [-p API_PASS]

## Using ONTAP REST API Python Client Library 

The Python client library is a package you can use when writing scripts to access the ONTAP REST API. It provides support for several underlying services, including connection management, asynchronous request processing, and exception handling. By using the Python client library, you can quickly develop robust code to support the automation of your ONTAP deployments.

### Software requirements:

Before installing the Python client library, you must make sure the following packages are installed on your system:

    * python 3.5 or later
    * requests 2.21.0 or later
    * marshmallow 3.2.1 or later

### Installing and importing the package :

You must install the package using the pip utility:

    * pip install netapp-ontap

After installing the package, you can import the objects you need into your application:

    * from netapp_ontap.resources import Volume, Snapshot

The ONTAP_REST_API_Python_Client_Library folder contains samples scripts to illustrate how ONTAP REST API Python Client Libraries can be used.

Deploy the scripts with the appropriate parameters.

eg:-

python3 create_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a
                        AGGR_NAME -sz VOLUME_SIZE [-u API_USER] [-p API_PASS]

## Support

Report any issues to: https://github.com/NetApp/ontap-rest-api/issues . For any questions or concerns ,please mail to the following mail id: ng-ontap-restapi-queries@netapp.com or connect with us through [Slack](https://netapppub.slack.com/archives/C1E4AJHDM). 
