# ONTAP-REST-Python Examples

NetApp® ONTAP® version 9.6 and later includes support for an expansive RESTful web services API. In comparison to an ONTAPI® application, the REST API offers a vastly simplified and workflow-driven user experience, allowing you to perform multiple operations on the storage objects with a single API. REST is the industry standard for APIs and the ONTAP REST API provides a tremendous opportunity to automate your storage deployments.

This repository contains sample scripts illustrating how to use the ONTAP REST API. You can access the API through the Python client library, which is preferable in most situations. If needed, you can also connect directly to the API using the native capabilities provided with Python.

## Using the Python client library

The Python client library is a package you can use when writing scripts to access the ONTAP REST API. It provides support for several underlying services, including connection management, asynchronous request processing, and exception handling. By using the Python client library, you can quickly develop robust code to support the automation of your ONTAP deployments.

Before beginning, you need to install the library. See the following web site for requirements and download instructions, as well as documentation for the library: [PyPI netapp-ontap](https://pypi.org/project/netapp-ontap/)

The repository folder **python_client_library** contains samples scripts you can use to access the ONTAP REST API through the Python client library. You must run each of the scripts with the appropriate parameters. For example:

```
python3 create_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a AGGR_NAME
-sz VOLUME_SIZE [-u API_USER] [-p API_PASS]
```
