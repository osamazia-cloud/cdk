#!/usr/bin/env python3
import os

from aws_cdk import core
from testing_cdk.vpc import VPC as crossVPC
from testing_cdk.instance import Instance as crossInstance
from testing_cdk.vpc_nestedstack import VPC as nestedVPC
from testing_cdk.ec2_nestedstack import Instance as nestedInstance

app = core.App()
stack_vpc=crossVPC(app, "sharjeelVPCStackDev")
crossInstance(app, "sharjeelinstanceDev",vpc=stack_vpc.vpc)

#calling nested stack
main_stack = core.Stack(app, 'NestedStack', env={'region': 'us-east-1'})
nested_stack_vpc = nestedVPC(main_stack, "nestedstackVPCdev")
nestedInstance(main_stack, "nestedstackInstacncedev", vpc=nested_stack_vpc.vpc)

app.synth()