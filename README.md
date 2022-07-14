# ONTAP-REST-Python Examples

NetApp® ONTAP® 9.6 and later versions include support for an expansive RESTful web services API. In comparison to an ONTAPI® application, the REST API offers a vastly simplified and workflow-driven user experience, allowing you to perform multiple operations on the storage objects with a single API. REST is the industry standard for API development and the ONTAP REST API provides a great opportunity to automate your storage deployments.

This repository contains sample scripts illustrating how to use the ONTAP REST API. You can access the API through the Python client library, which is preferable in most situations. If needed, you can also connect directly to the API using the native capabilities provided with Python. See the repository folder **examples** with two subfolders containing sample code by usage type. Also see the folder **lod** for instructions on using the NetApp Lab on Demand (LOD) to run the sample scripts.

## Using the Python client library

The Python client library is a package you can use when writing scripts to access the ONTAP REST API. It provides support for several underlying services, including connection management, asynchronous request processing, and exception handling. By using the Python client library, you can quickly develop robust code to support the automation of your ONTAP deployments.

Before beginning, you need to install the package containing the library. For example:

```
pip install netapp-ontap
```

You should also review the [PyPI netapp-ontap](https://pypi.org/project/netapp-ontap/) package web page for detailed system requirements and further instructions, as well as reference documentation for the library.

The repository folder **examples/python_client_library** contains sample scripts to access the ONTAP REST API through the Python client library. You need to run each of the scripts with the appropriate parameters. Use the help provided with each script to get started. For example:

```
python3 list_volume.py -h
```

## Directly accessing the ONTAP REST API

The repository folder **examples/rest_api** contains sample scripts to directly access the ONTAP REST API using the `requests` library. You need to run each of the scripts with the appropriate parameters. Use the help provided with each script to get started. For example:

```
python3 create_volume.py -h
```

## Running the sample scripts in the Lab on Demand

You can run the sample scripts in the NetApp Lab on Demand (LOD). The repository folder [lod](https://github.com/NetApp/ontap-rest-python/tree/master/lod) contains instructions as well as the initialization script needed to configure the LOD environment.

## Support

Report any issues to: https://github.com/NetApp/ontap-rest-api/issues. For any questions or concerns, send an email to: ng-ontap-restapi-queries@netapp.com, post on the [community forums](https://community.netapp.com/t5/ONTAP-Rest-API-Discussions/bd-p/ONTAP-Rest-API-discussions) or connect with us through [Slack](https://netapppub.slack.com/archives/C1E4AJHDM).

To learn more about ONTAP REST APIs, visit https://devnet.netapp.com/restapi.php 
