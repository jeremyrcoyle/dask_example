First, see the [AWS Setup](aws_setup.md) documentation, for tips on how to set up AWS and the AWS CLI for use in this example

# Installation
1. clone the repo `git clone https://github.com/jeremyrcoyle/dask_utils.git`
2. install dependencies `pip install -r requirements.txt`
3. modify *to be created* `cluster_def.cfg` file


# Usage
1. Spool up cluster `./start_ec2_cluster.sh`
	* for now need to manually provision `dask_utils.py`
2. SSH into cluster `dask-ec2 ssh`
3. Pull in needed code using *http (not SSH!)* link on bitbucket (e.g. `git clone https://jrcoyle@bitbucket.org/ICCTnaya/ais_analysis.git`) 
4. Run code (e.g. python `)