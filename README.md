# ONTAP-REST-API
Sample scripts for illustrating the use of ONTAP REST APIs and  ONTAP REST API Python Client Libraries.

The ONTAP_REST_API folder contains samples scripts to illustrate how ONTAP REST APIs can be used.

Deploy the scripts with the appropriate parameters.

eg:-

python3 create_volume_pcl.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a
                            AGGR_NAME -sz VOLUME_SIZE [-u API_USER]
                            [-p API_PASS]

The ONTAP_REST_API_Python_Client_Library folder contains samples scripts to illustrate how ONTAP REST API Python Client Libraries can be used.

Deploy the sscripts with the appropriate parameters.

eg:-

python3 create_volume.py [-h] -c CLUSTER -v VOLUME_NAME -vs SVM_NAME -a
                        AGGR_NAME -sz VOLUME_SIZE [-u API_USER] [-p API_PASS]

