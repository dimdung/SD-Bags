dimdung:boto3 dimdung$ cat ec2-create.py 
#!/usr/bin/python

import boto

ec2_connection = boto.connect_ec2('Access_Key','aws-secret-key'')
vpc_connection = boto.connect_vpc('Access_Key','aws-secret-key')

ec2_connection.run_instances('ami-60b6c60a', instance_type='t2.micro', key_name="kp-web-mgmt-e" )
dimdung:boto3 dimdung$ cat s3-dev.py 
#!/usr/bin/python

import boto

conn= boto.connect_s3('Access_Key','aws-secret-key')

bucket = conn.create_bucket('test')
#bucket = conn.delete_bucket('dimdung3')
#bucket = conn.delete_bucket('dimdung-test')


dimdung:boto3 dimdung$ cat ec2-terminate.py 
import boto

ids = ['i-b2318703', 'i-d1bf0e60']
ec2_connection = boto.connect_ec2('Access_Key','aws-secret-key')
vpc_connection = boto.connect_vpc('Access_Key','aws-secret-key')

ec2_connection.terminate_instances(instance_ids=ids)


dimdung:boto3 dimdung$ 
