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
  ip = instance.ip
  username = instance.username
  keypair = os.path.expanduser(instance.keypair)
  base_cmd = ['ssh', username + '@' + ip]
  base_cmd = base_cmd + ['-i', keypair]
  base_cmd = base_cmd + ['-oStrictHostKeyChecking=no']
  base_cmd = base_cmd + ['-p %i' % instance.port]
  run_script = ["'bash -s' < provision_script.sh"]
  full_cmd=string.join(base_cmd + run_script)
  
  #clone dask_utils on cluster
  print(full_cmd)
  os.system(full_cmd)
  
  #copy cluster.yaml up
  scp_cmd = ['scp']
  scp_cmd = scp_cmd + ['-P %i' % instance.port]
  scp_cmd = scp_cmd + ['-i', keypair]
  scp_cmd = scp_cmd + ['cluster.yaml', username + '@' + ip + ":cluster.yaml"]
  
  full_scp=string.join(scp_cmd)
  print(full_scp)
  os.system(full_scp)


if __name__ == "__main__":
    main()