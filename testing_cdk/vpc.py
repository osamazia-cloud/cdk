from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
    core
)
# from aws_cdk import core

class VPC(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            self.node.try_get_context("vpc_name"),
            max_azs = self.node.try_get_context("max_azs"),
            vpc_name = self.node.try_get_context("vpc_name"),
            cidr = self.node.try_get_context("vpc_cidr"),
            subnet_configuration = [
                ec2.SubnetConfiguration(
                    name="public-dev",
                    cidr_mask=kwargs.get("subnet_cidr_mask", 24),
                    subnet_type=ec2.SubnetType.PUBLIC
                ),
                ec2.SubnetConfiguration(
                    name="private-dev",
                    cidr_mask=kwargs.get("subnet_cidr_mask", 24),
                    subnet_type=ec2.SubnetType.PRIVATE
                )
            ]
        )

        core.CfnOutput(
            scope=self,
            id="vpc_id",
            value=self.vpc.vpc_id,
            export_name="vpcdev"
        )

        core.CfnOutput(
            scope=self,
            id="public_subnets",
            value=','.join([x.subnet_id for x in self.vpc.public_subnets]),
            export_name="public-subnets"
        )