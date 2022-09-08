from aws_cdk.aws_apigateway import AuthorizationType, MethodOptions
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda, aws_apigateway,
)

from aws_cdk_snyk.hitcount import HitCounter


class AwsCdkSnykStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = aws_lambda.Function(
            self,
            'HelloHandler',
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
            environment={
                'MySecret': 'secretstring1234'
            }
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda
        )

        aws_apigateway.LambdaRestApi(
            self,
            'Endpoint',
            handler=hello_with_counter._handler,
            default_method_options=MethodOptions(authorization_type=AuthorizationType.NONE)
        )
