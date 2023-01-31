# EC2 Instance Start/Stop Script using boto3

This script allows you to start and stop an EC2 instance using the AWS SDK (boto3). The script uses the `boto3` library to interact with the AWS EC2 service and perform the necessary actions.

## Requirements

- Python 3.x installed on your machine
- `boto3` library installed (`pip install boto3`)


## Usage


1. Run the script using the following command to start the instance: `python3 start_ec2.py`
2. Run the script using the following command to stop the instance: `python3 stop_ec2.py`
3. Run the script using the following command to update the instance Security group rule with your IP address: `python3 update_sg_ssh_ipaddrs.py`

## Output

The script will start or stop the  EC2 instance and return a message indicating the action taken.

## Getting on the Server
Run this command on terminal in the location of myrsa2 (Make sure the file permission is 0400): `ssh -i "myrsa2.pem" ubuntu@ec2-34-224-16-79.compute-1.amazonaws.com`


## Conclusion

This script provides a simple and automated way to start and stop an EC2 instance using Python and the boto3 library. By automating this process, you can save time and ensure consistent and reliable behavior for your EC2 instances. Then you can ssh to the server and stop the instance when you done.
# Ec2_start-stop_Script
