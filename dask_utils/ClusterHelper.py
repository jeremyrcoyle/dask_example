from dask_ec2 import Cluster, EC2
from dask.distributed import Client, progress
import os

def destroy_cluster():
  cluster = Cluster.from_filepath("~/cluster.yaml")

  driver = EC2(region=cluster.region, default_vpc=False, default_subnet=False)
  worker_ids = [i.uid for i in cluster.instances[1:]]
  scheduler_ids = [cluster.instances[0].uid] 

  print("Terminating workers")
  driver.destroy(worker_ids)
  print("Terminating scheduler")
  driver.destroy(scheduler_ids)
  print("Deleting cluster file")
  os.remove("cluster.yaml")

if __name__ == "__main__":
    destroy_cluster()