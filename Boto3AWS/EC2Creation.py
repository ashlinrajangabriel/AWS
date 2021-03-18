import boto3

ec2 = boto3.client('ec2')
ec2.describe_instances()


resp = ec2.create_key_pair( KeyName = 'GabrielKeyPair')
print(resp['KeyMaterial'])

#Now also i need to use this Key Material to access later on my ec2 instance.

file = open('GabrielResource.pem', 'w')
file.write(resp['KeyMaterial'])
file.close
print('file written')

#Lets check for security Group
GroupLists = ec2.describe_security_groups()
print(GroupLists)

#Creating new security group
V_CreateGroupID = ec2.create_security_group (
GroupName = 'GabrielGroup' ,
Description  = 'Description of Gabriel Group',
VpcId  =  'vpc-er344300356XX'
)
print("Group ID created")
gid = V_CreateGroupID['GroupId']
print(gid)

ec2.authorize_security_group_ingress(
    GroupId = gid,
        IpPermissions = [
            {
                'IpProtocol' : 'tcp',
                'FromPort' : 80,
                'ToPort' : 80,
                'IpRanges' : [{'CidrIp' : '0.0.0.0/0'}]
            },
            {
                'IpProtocol' :  'tcp',
                'FromPort' : 22,
                'ToPort' : 22,
                'IpRanges' : [{'CidrIp': '0.0.0.0/0'}]
            }
        ]
)



# #Creating EC2 Instance
def create_instance():

    ec2_client = boto3.client("ec2", region_name="eu-west-1")
    instances = ec2_client.run_instances(
        ImageId="ami-079d9017cb651564d",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="GabrielKeyPair",
        BlockDeviceMappings = [
            {
                'DeviceName' : "/dev/xvda",
                'Ebs' : {
                    'DeleteOnTermination': True,
                    'VolumeSize': 20
                }
            }
        ],
        SecurityGroups = ['GabrielGroup']
    )
    print(instances["Instances"][0]["InstanceId"])

create_instance()
