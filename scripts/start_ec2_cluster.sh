#!/bin/bash

# export AWS_PROFILE=icct
dask-ec2 up --keyname aws --keypair ~/.ssh/aws.pem \
			--region-name us-west-2 --ami ami-37198657 \
			--tags testkey:testvalue \
			--type m4.large --count 10 \
			--iaminstance-name S3role
			
