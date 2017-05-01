First, see the [AWS Setup](aws_setup.md) documentation, for tips on how to set up AWS and the AWS CLI for use in this example

# Installation
1. clone the repo `git clone https://github.com/jeremyrcoyle/dask_utils.git`
2. install dependencies `pip install -r requirements.txt`

# Usage
1. Modify `start_ec2_cluster.sh`, to define the cluster you want to start including ssh key, AMI instance type, and node type and number of nodes.

__todo:__ add support for a configuration file to make this easier

2. Spool up cluster `./start_ec2_cluster.sh`
    * when this script is done running, it will give a url where you can check on cluster behavior
3. Install `dask_utils` on the cluster: `python provision_dask_utils.py`

__todo:__ do this automatically with salt

4. SSH into cluster `dask-ec2 ssh`
5. Pull in needed code using *http (not SSH!)* link on bitbucket:
    e.g. `git clone https://jrcoyle@bitbucket.org/ICCTnaya/ais_analysis.git`
6. Install dependencies for the code: 
``` sh
cd ais_analysis.git
pip install -r requirements.txt
```

__NB this only installs dependencies on the scheduler__

__todo:__ add support for creating a salt state that installs dependencies on all nodes

7. Run code (e.g. `python do_LinearInterpolation.py`)
8. Monitor progress
    * Use the cluster monitoring tool (link provided by the `./start_ec2_cluster.sh` script)
    * You can also inspect the CPU activity of the nodes in AWS Web Console 
9. Shut down cluster
    * Run `python destroy_cluster.py`
    * __todo:__ build capacity to shutdown cluster automatically when a job is finished
 