First, see the [AWS Setup](aws_setup.md) documentation, for tips on how to set up AWS and the AWS CLI for use in this example


```dask-ec2 up --keyname aws --keypair ~/.ssh/aws.pem --region-name us-west-1 --ami ami-bc4461dc --tags test-cluster```

note [https://cryptography.io/en/latest/installation/#building-cryptography-on-macos]