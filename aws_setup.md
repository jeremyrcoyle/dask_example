# AWS Setup

### Create IAM

This creates a user with certain permissions that can be used to execute commands on AWS
[https://console.aws.amazon.com/iam/]
1. Create user
2. Specify needed permissions (depends on application)
3. Download credentials as csv file

### Setup AWS CLI 

The AWS CLI tool is a command line interface to all of AWS
Follow directions here to install the CLI tool: [http://docs.aws.amazon.com/cli/latest/userguide/installing.html]
After it's installed, configure it with the credentials generated above.
In a terminal, type 
```aws configure```. 

When prompted, provide the keys in the credentials.csv file.
It will also ask for a region. It's important to use the same region throughout this tutorial, as it can be difficult to get different AWS components in different regions to work well together. Pick one close to your physical location. For example, `us-west-1` is in Northern California.

When you're done, be sure to delete the credentials.csv file you downloaded.
 
### Generate EC2 SSH key
Generating an SSH key for EC2 will allow you (and your software) to connect to EC2 instances remotely without requiring a password.

The below script uses the AWS CLI to generate a key, and move it to a common place keys are stored on your system.

```sh
aws ec2 create-key-pair --key-name aws --query 'KeyMaterial' --output text > aws.pem
mv aws.pem ~/.ssh/aws.pem
chmod 400 ~/.ssh/aws.pem 
```
