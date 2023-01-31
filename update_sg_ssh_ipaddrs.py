import boto3
import botocore
import requests
import configparser



def update_security_group_rule(security_group_id, port, access_key, secret_key, rule_id=None):
    
    try:
        # Get the current IP address of the machine
        ip = requests.get("http://checkip.amazonaws.com").text.strip()

        # Connect to EC2 using the specified access key and secret key
        ec2 = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

        # Get the current rules in the security group
        response = ec2.describe_security_groups(
            GroupIds=[security_group_id],
        )

        # Find the desired rule to update
        for security_group in response['SecurityGroups']:
            for permission in security_group['IpPermissions']:
                for range in permission['IpRanges']:
                    if rule_id and str(rule_id) == str(range.get("RuleId", "")):
                        # Update the desired rule
                        range['CidrIp'] = f"{ip}/32"
                        range['Description'] = "Favor IP Address"
                        ec2.revoke_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[permission]
                        )
                        ec2.authorize_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[permission]
                        )
                        print(f"Successfully updated security group rule {rule_id} with IP address {ip} on port {port}")
                        return
                    elif not rule_id and range['CidrIp'] == f"{ip}/32":
                        # Update the first rule with the current IP address
                        range['CidrIp'] = f"{ip}/32"
                        range['Description'] = "Favor IP Address"
                        ec2.revoke_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[permission]
                        )
                        ec2.authorize_security_group_ingress(
                            GroupId=security_group_id,
                            IpPermissions=[permission]
                        )
                        print(f"Successfully updated security group rule {rule_id} with IP address {ip} on port {port}")
                        return
        # Add the current IP address to the security group if no rule was found
        ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {
                    'FromPort': port,
                    'ToPort': port,
                    'IpProtocol': 'TCP',
                    'IpRanges': [
                        {
                            'CidrIp': f"{ip}/32",
                            'Description': "Favor IP Address"
                        },
                    ],
                },
            ],
        )


        print(f"Successfully added {ip} to security group {security_group_id} on port {port}")
    
    except botocore.exceptions.ClientError as error:
        # Handle the duplicate rule error
        if error.response['Error']['Code'] == 'InvalidPermission.Duplicate':
            print(f"The specified rule for {ip} already exists")
        else:
            raise error


if __name__ == "__main__":
    
    port = 22  # Replace with the desired port number

    # Load the AWS keys from the config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    security_group_id = config['AWS']['security_group_id']
    rule_id = config['AWS']['rule_id']
    access_key = config['AWS']['access_key']
    secret_key = config['AWS']['secret_key']
    update_security_group_rule(security_group_id, port, access_key, secret_key, rule_id)
