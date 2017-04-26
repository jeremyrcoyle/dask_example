import csv
import numpy as np
import dask.dataframe as dd
from distributed import Client, LocalCluster

csv_filename = 'example_data.csv'
# Generate very large dataset
print("Generating data\n")
n = int(1e7)


csv_file = open(csv_filename, "wb")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['id', 'value'])


for i in xrange(n):
  row_id = np.random.randint(0, 10)
  row_value = np.random.randn()
  csv_writer.writerow([row_id, row_value])
csv_file.close()

# setup cluster and use dask
print("Creating distributed cluster\n")
cluster = LocalCluster()
client = Client(cluster)

print("Computing means\n")
example_dd = dd.read_csv(csv_filename)
results = example_dd.groupby(example_dd.id).value.mean().compute()

print("Saving results\n")
results.to_csv('results.csv')

cluster.close()
