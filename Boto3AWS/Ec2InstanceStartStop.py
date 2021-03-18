import boto3

ec2 = boto3.client('ec2')
#print(ec2.describe_instances())
instancesDetails = ec2.describe_instances()
#print("-->", instancesDetails['Reservations'][0]["Instances"][0]["InstanceId"])
InstanceValue = instancesDetails['Reservations'][0]["Instances"][0]["InstanceId"]
#ec2.stop_instances(InstanceIds = [InstanceValue] ) #To stop the instance
ec2.start_instances(InstanceIds = [InstanceValue] )  #To start the instances
#ec2.terminate_instances(InstanceIds = [InstanceValue] )  #Terminates the instances
#["Instances"][0]["InstanceId"])
