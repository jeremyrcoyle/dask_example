#!/bin/python
import yaml
import os
from voluptuous import Schema, Required, All, Length, Range
from dask_ec2.cluster import Cluster
from dask_ec2.salt import upload_pillar



#schema for yaml config
schema = Schema({Required('keyname'): All(str,Length(min=1)),
                 Required('keypair'): All(str,Length(min=1)),
                 Required('region-name'): All(str,Length(min=1)), 
                 Required('ami'): All(str,Length(min=1)),
                 Required('type'): All(str,Length(min=1)),
                 Required('count'): All(int,Range(min=2,max=100)),
                 Required('iaminstance-name'): All(str,Length(min=1))})


config_file="example_configs/example1.yaml"

def cluster_from_config(config_file):
  
  with open(config_file,"r") as stream:
    # load cluster config from file
    try:
        parsed_config=(yaml.load(stream))
    except yaml.YAMLError as exc:
        raise Exception("Couldn't parse config file")

    try:
        if(len(parsed_config) > 1):
            raise Exception("Found multiple cluster definitions in one file, not currently supported")
        cluster_name = parsed_config.keys()[0]        
        cluster_config = parsed_config[cluster_name]
    except:
        raise Exception("Invalid config file")
    
    # validate cluster config fields
    schema(cluster_config)

    # use name to name cluster.yaml filename (these should be unique if running multiple clusters simultaneously)
    cluster_file = "%s.yaml" % cluster_name
    cluster_config['cluster_file'] = cluster_file
    
    if(os.path.exists(cluster_file)):
        raise Exception("Cluster file already exists. Your cluster may already be running. Giving up...")
        
    # for now let's be lazy and just call the dask-ec2 CLI    
    # todo: spin this up ourselves and be smarter about how we handle failures
    cluster_command = """dask-ec2 up --file %(cluster_file)s \
    --keyname %(keyname)s --keypair %(keypair)s \
    --region-name %(region-name)s --ami %(ami)s \
    --tags testkey:testvalue \
    --type %(type)s --count %(count)s \
    --iaminstance-name %(iaminstance-name)s"""
                            
          
    full_command = cluster_command % cluster_config

    print("Starting cluster. This is going to take a while")
    print(full_command)
    cluster_up_return = os.system(full_command)
    if not(cluster_up_return==0):
        print("Something may have gone wrong with the cluster start. Consider destroying the cluster and trying again")
    
    return(cluster_file)
# print("Cluster running. Now provisioning packages")
# cluster = Cluster.from_filepath(filepath)
# output = cluster.salt_call("*", "state.sls", ["conda"])
    
def add_custom_salt(cluster_file):
from dask_ec2.cli.main import print_state
cluster = Cluster.from_filepath(cluster_file)
output = cluster.salt_call("*", "state.sls", ["conda"])
print_state(output)
#git+https://jrcoyle@bitbucket.org/ICCTnaya/ais_analysis.git
if __name__ == "__main__":
    cluster_from_config(config_file)