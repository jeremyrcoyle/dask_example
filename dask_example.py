import csv
import numpy as np
import dask.dataframe as dd
import boto
from boto import ec2
from dask.distributed import Client, progress
import os
import s3fs
from dask_ec2 import Cluster
csv_filename = 's3://ais-2013/example_data.csv'
# start process using dask-ec2 code (with options carefully chosen)
# avoid CLI version if possible
# reset iam roles
# restart client

# s3 = s3fs.S3FileSystem()
# s3.ls('ais-2013')
# s3.head(csv_filename)
os.environ['AWS_PROFILE'] = 'icct'

client = Client('34.208.115.209:8786')


# # Generate very large dataset
# print('Generating data\n')
# n = int(1e7)


# csv_file = open(csv_filename, 'wb')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['id', 'value'])


# for i in xrange(n):
#   row_id = np.random.randint(0, 10)
#   row_value = np.random.randn()
#   csv_writer.writerow([row_id, row_value])
# csv_file.close()

# # setup cluster and use dask
# print('Creating distributed cluster\n')
# cluster = LocalCluster()
# client = Client(cluster)

print('Computing means\n')
example_dd = dd.read_csv(csv_filename)
# , storage_options = {'key': 'use-instance-role-credentials'})
results = example_dd.groupby(example_dd.id).value.mean().compute()

print('Saving results\n')
results.to_csv('results.csv')

cluster.close()
