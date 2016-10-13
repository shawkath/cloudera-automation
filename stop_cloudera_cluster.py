
# Created By : Shawkath Khan
# Created On : October 19 2015
# Purpose    : To stop the cloudera cluster & services in Python using boto package



from cm_api.api_client import ApiResource
import socket
import time
import boto.ec2
import time
import logging

logging.basicConfig()

AKID='AKIAJITZTIGJKVLJGLIGFHYQ'
ASAK='cyZ7109J0Vkn07KgfiuNLKnmMPKdf'
REGION='us-west-1'

conn = boto.ec2.connect_to_region(REGION, aws_access_key_id=AKID, aws_secret_access_key=ASAK)


# HOSTNAME OR IP OF THE MACHINE WHERE CLOUDERA MANAGER IS INSTALLED
CM_HOST="<<ENTER_YOUR_CLOUDERA_IP>>"


api = ApiResource(CM_HOST, version=10, username='<<ENTER_CLOUDERA_MANAGER_USERNAME>>', password='<<ENTER_CLOUDERA_MANAGER_PASSWORD>>')
dev01 = api.get_cluster('<<ENTER_YOUR_CLOUDERA_CLUSTERNAME>>')

# STOP ALL CLOUDERA SERVICES
print ">> STOPPING ALL SERVICES UNDER CLUSTER "
dev01.stop().wait()

# SLEEP FOR 20 SECONDS FOR THE SERVICES TO BE DOWN
time.sleep(20)


