import os
import subprocess

from dask_ec2 import Cluster
from dask.distributed import Client, progress
import sys
import subprocess
import os
import string
def main():
  cluster = Cluster.from_filepath('cluster.yaml')
  instance = cluster.instances[0]
  for instance in cluster.instances:
    ip = instance.ip
    username = instance.username
    keypair = os.path.expanduser(instance.keypair)
    base_cmd = ['ssh', username + '@' + ip]
    base_cmd = base_cmd + ['-i', keypair]
    base_cmd = base_cmd + ['-oStrictHostKeyChecking=no']
    base_cmd = base_cmd + ['-p %i' % instance.port]
    run_script = ["'sudo apt-get -y install libgeos-dev'"]
    full_cmd=str.join(' ', base_cmd + run_script)
    
    #clone dask_utils on cluster
    print(full_cmd)
    os.system(full_cmd)

if __name__ == "__main__":
    main()
