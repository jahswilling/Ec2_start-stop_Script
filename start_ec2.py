import boto3
import configparser

# Load the AWS keys from the config file
config = configparser.ConfigParser()
config.read('config.ini')
access_key = config['AWS']['access_key']
secret_key = config['AWS']['secret_key']
region_name = config['AWS']['region_name']
instance_id = config['AWS']['instance_id']

# Initialize a session using DigitalOcean Spaces.
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region_name
)

# Get the EC2 resource
ec2 = session.resource('ec2')

# Get the EC2 instance
instance = ec2.Instance(instance_id)

def start_instance():
    instance.start()
    print(f'Started instance {instance_id}')


# Use the below code to start the instance
start_instance()

