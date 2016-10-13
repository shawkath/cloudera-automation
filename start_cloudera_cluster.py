
# Created By : Shawkath Khan
# Created On : October 19 2015
# Purpose    : To start the cloudera cluster & services in Python using boto package



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



print ">> STARTING ALL SERVICES UNDER CLUSTER "
dev01.start().wait()

# LIST OF SERVICES
arrServices = [ 'hue', 'impala', 'zookeeper', 'oozie', 'hdfs', 'solr2', 'hbase', 'yarn', 'hive'];


print ">> LISTING ALL ACTIVE HOSTS "

# LIST ALL THE HOSTS UNDER CM_HOST
for h in api.get_all_hosts():
    print h.hostname

# GET A LIST OF ACTIVE CLUSTERS
print ">> LISTING ALL ACTIVE CLUSTERS  "
cdh4 = None
for c in api.get_all_clusters():
  print c.name
  if c.version == "CDH5":
    cdh5 = c

# GET A LIST OF ACTIVE SERVICES

print ">> LISTING ALL SERVICES "
for s in cdh5.get_all_services():
  print s
  if s.type == "HDFS":
    hdfs = s

# GET A LIST OF ALL SERVICES AND THEIR CURRENT STATUSES
print ">> LISTING ALL SERVICES & STATUSES "
for serviceName in arrServices:
        service = dev01.get_service(serviceName)
        
        print '* * *' + serviceName + '* * *'

        # IF ANY SERVICES ARE NOT STARTED, FORCE START THEM
        if (service.serviceState != "STARTED"):
                print serviceName + ' service is down; Restarting...please wait'
                service.restart()
                # WAIT FOR 20 SECONDS TO ENSURE THE SERVICE IS STARTED
                time.sleep(20)
                # GET CURRENT STATUS OF THE SERVICE AFTER FORCE RESTART
                print 'Service status after restart: ' + service.serviceState        
        else:
                print serviceName + ' is ' + service.serviceState        
        


