# Create a bucket, in this case emerald_test_bucket
from os import environ

from boto import connect_s3

AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_KEY = environ['AWS_SECRET_KEY']

conn = connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_KEY)
conn.create_bucket('emerald_test_bucket')
