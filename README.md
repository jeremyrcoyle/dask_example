First, see the [AWS Setup](aws_setup.md) documentation, for tips on how to set up AWS and the AWS CLI for use in this example

1. Spool up cluster `./start_ec2_cluster.sh`
2. SSH into cluster `dask-ec2 ssh`
3. Pull in needed code using *http (not SSH!)* link on bitbucket (e.g. `git clone https://jrcoyle@bitbucket.org/ICCTnaya/ais_analysis.git`) 
4. Run code (e.g. python `)