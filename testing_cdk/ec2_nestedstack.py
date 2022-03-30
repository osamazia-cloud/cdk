from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    core
)


class Instance(core.NestedStack):
    def __init__(self, scope: Construct, construct_id: str,vpc:ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ssh_tunnel_role = iam.Role(
            self,
            "ssh_tunnel_role"+"-"+construct_id,
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            role_name='ssh_tunnel_role'
        )

        ssh_tunnel_role.add_to_policy(iam.PolicyStatement(
            resources=["*"],
            actions=[
                "secretsmanager:GetSecretValue"                ]
        ))

        iam.CfnInstanceProfile(
            self,
            id="ssh_tunnel_profile"+"-"+construct_id,
            roles=[ssh_tunnel_role.role_name],
            instance_profile_name="ssh_tunnel_instance_profile",
        )

        with open('./testing_cdk/user_data.sh', 'r') as f:
            user_data = f.read()
        ec2.CfnInstance(
            self,
            construct_id,
            image_id="ami-0c02fb55956c7d316",
            instance_type="t2.micro",
            key_name="OsamaKP",
            security_group_ids=["sg-00463a7141fafa949-123"],
            subnet_id="subnet-0c5eb1c31ae288a15" ,
            iam_instance_profile="ssh_tunnel_instance_profile",
            user_data=core.Fn.base64(user_data)
        )
