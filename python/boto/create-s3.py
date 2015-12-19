[ec2-user@ip-172-31-56-237 ~]$ ls
dev.py
[ec2-user@ip-172-31-56-237 ~]$ cat dev.py
#!/usr/bin/python
import boto
conn = boto.connect_s3()
#bucket = conn.create_bucket('dimdung-test1')
bucket = conn.delete_bucket('dimdung-test1')
#print "Creating S3 bucket %s" % bucket


[ec2-user@ip-172-31-56-237 ~]$
