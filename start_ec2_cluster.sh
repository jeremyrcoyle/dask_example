#!/bin/bash

export AWS_PROFILE=icct
dask-ec2 up --keyname icct --keypair ~/.ssh/icct.pem \
			--region-name us-west-2 --ami ami-37198657 \
			--tags testkey:testvalue \
			--type m4.large --count 2 \
			--iaminstance-name S3role
			
