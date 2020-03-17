# ONTAP-REST-API

NetApp® ONTAP® version 9.6 and later includes support for an expansive RESTful web services API. In comparison to the ONTAPI® application, the REST API offers a vastly simplified and workflow-driven user experience, allowing you to perform multiple operations on the storage objects with a single API. REST is the industry standard for APIs and provides a tremendous opportunity to automate your storage deployments.

This repository contains sample scripts that illustrate how to use the ONTAP REST API. You can access the REST API through the Python client library, which is preferable in most situations. If needed, you can also connect directly to the API using the native capabilities provided with Python.

## Using the Python client library

The Python client library is a package you can use when writing scripts to access the ONTAP REST API. It provides support for several underlying services, including connection management, asynchronous request processing, and exception handling. By using the Python client library, you can quickly develop robust code to support the automation of your ONTAP deployments.

Before you begin, you need to install the library. See the following location for xxx

The folder *python_client_library* contains samples scripts you can use to access the ONTAP REST API through the Python client library. You must run each of the scripts with the appropriate parameters. For example:

```
python3 create_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a AGGR_NAME -sz VOLUME_SIZE [-u API_USER] [-p API_PASS]
```

## Directly accessing the ONTAP REST API

The folder *rest_api* contains samples scripts you can use to directly access the ONTAP REST API through Python. You must run each of the scripts with the appropriate parameters. For example:

```
python3 create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a AGGR_NAME -sz VOLUME_SIZE [-u API_USER] [-p API_PASS]
```

## Support

Report any issues to: https://github.com/NetApp/ontap-rest-api/issues . For any questions or concerns, send an email to: ng-ontap-restapi-queries@netapp.com or connect with us through [Slack](https://netapppub.slack.com/archives/C1E4AJHDM).
