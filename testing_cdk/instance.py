from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class Instance(core.Stack):

    def __init__(self, scope: Construct, construct_id: str,vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        ec2.Instance(
        self, 
        construct_id,
        instance_type = ec2.InstanceType("t2.micro"), 
        machine_image = ec2.MachineImage.latest_amazon_linux(),
        vpc = vpc,
        # vpc = core.Fn.import_value(shared_value_to_import="vpc_dev"),
        instance_name="nginxDev",
        key_name="sharjeel_key",
        user_data=ec2.UserData.add_execute_file_command( self, file_path="./user_data.sh")
        )