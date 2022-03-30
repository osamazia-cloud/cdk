from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    core
)

class CdkSecurityGroup(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        security_group = ec2.SecurityGroup(
            self,
            "SG",
            security_group_name="devsecurity",
            #vpc = core.Fn.split(",", core.Fn.import_value("vpc_dev")),
            
            allow_all_outbound=False
        )

        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80)
        )