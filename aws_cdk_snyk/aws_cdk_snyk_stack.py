from aws_cdk.aws_apigateway import AuthorizationType, MethodOptions
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda, aws_apigateway,
)


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

        aws_apigateway.LambdaRestApi(
            self,
            'Endpoint',
            handler=my_lambda,
            default_method_options=MethodOptions(authorization_type=AuthorizationType.NONE)
        )
