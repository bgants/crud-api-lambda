import aws_cdk as core
import aws_cdk.assertions as assertions

from crud_api_lambda.crud_api_lambda_stack import CrudApiLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in crud_api_lambda/crud_api_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CrudApiLambdaStack(app, "crud-api-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
