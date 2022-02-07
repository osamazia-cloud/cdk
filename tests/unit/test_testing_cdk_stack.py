import aws_cdk as core
import aws_cdk.assertions as assertions

from testing_cdk.testing_cdk_stack import TestingCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in testing_cdk/testing_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestingCdkStack(app, "testing-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
