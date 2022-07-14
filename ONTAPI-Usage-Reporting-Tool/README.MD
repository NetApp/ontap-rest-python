ONTAPI Usage Reporting Tool
---------------------

 * Introduction
 * Requirements
 * Usage
 * Support

INTRODUCTION
------------
In order to help our professional services, Customers and Partners to help them identify the ONTAPI usage in their cluster environment, ONTAPI Usage Reporting tool has been developed covering 3 different usecases. 
These scripts are python-based.

The scripts provided in this wheel file:

Script        |  Description
------------- | -------------
**apache_scraper.py**  | Apache log scraper to find ONTAPIs (ZAPIs) called against ONTAP nodes
**session_stats.py**   | Command line script to pull session statistics data from ONTAP
**zapi_to_rest.py**    | Script to find REST details of ZAPI and attributes passed


REQUIREMENTS
-------------

Python3.7 or higher is required to run the scripts. If there are compatibility issues with the the included packages, All versions offered can be found below:

* numpy - https://pypi.org/project/numpy/#files
 
* pandas - https://pypi.org/project/pandas/#files

* python-dateutil - https://pypi.org/project/python-dateutil/#files

* pytz - https://pypi.org/project/pytz/#files

* requests - https://pypi.org/project/requests/#files

* six - https://pypi.org/project/six/#files

Command to install the wheel file: **pip install netapp_ztools-1.0.0-py3-none-any**

USAGE
-----

####  Script_1: python apache_scraper.py -h ####

- **Description:** Apache log scraper to find ONTAPIs (ZAPIs) called against ONTAP nodes

- **usage:** - apache_scraper.py [-h] [-unique] [-start START] [-end END] [-date DATE] [-node NODE] [-write-csv] [-verbose] log

- positional arguments:
  - log&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Absolute path of apache_access.log file copied from an ONTAP node

- optional arguments:
  - -h,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;help show this help message and exit
  - -unique&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Filter unique ZAPIs only
  - -start START&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Start time to inspect logs, formatted as H:M:S
  - -end END&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;End time to inspect logs, formatted as H:M:S
  - -date DATE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date of filtered results if a multiday run
  - -node NODE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Node to search
  - -write-csv, -w&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Writes to a csv file
  - -verbose, -v 
![image](https://user-images.githubusercontent.com/61284863/153816578-0842a8b0-97d9-4a1c-90f3-358ecc5f589c.png)


#### Script_2: python session_stats.py -h ####

- **Description:** Command line script to pull session statistics data from ONTAP

- **usage:** session_stats.py [-h] [-username USERNAME] [-password PASSWORD] [-scope SCOPE] [-sort-by SORT_BY] [--verbose] [-write-csv] hosts

- positional arguments:
  hosts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Comma separated list of IP addresses or FQDN of ONTAP node(s)

- optional arguments:
  - -h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit
  - -username&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;USERNAME
  - -password&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PASSWORD
  - -scope&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SCOPE{cluster|node}
  - -sort-by&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SORT_BY {application|location|request|user|vserver}
  - --verbose, -v
  - -write-csv, -w

The CLI equivalent of the session_stats.py commands is: **security session request-statistics show-by-{application|location|request|user|vserver}**

![image](https://user-images.githubusercontent.com/61284863/153811433-5b087671-eaf2-48dc-9a53-1f8007223f8f.png)

#### Script_3: python zapi_to_rest.py -h ####
--------------------------------
- **Description:** Tools to find REST details of ZAPI and attributes passed

- **usage:** zapi_to_rest.py [-h] [-attrs ATTRS] zapi

- positional arguments:
   - zapi&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ZAPI

- optional arguments:
  - -h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;show this help message and exit
  - -attrs ATTRS, -a ATTRS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comma separated list of attributes to map REST field equivalents
  - --version VERSION&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Specify target ONTAP version { 9_10_1 | 9_9_1 | 9_8 }

![image](https://user-images.githubusercontent.com/61284863/153816352-4b1fc5c0-ffe0-4356-9823-9ed3c6b51099.png)


SUPPORT
-----------

These scripts were developed by the CSI team at NetApp. For questions and for addressing bugs, please reach out to ng-ontap-rest-queries@netapp.com
Demo: [ONTAPI Usage Reporting Tool](https://www.youtube.com/watch?v=gJSWerW9S7o)
