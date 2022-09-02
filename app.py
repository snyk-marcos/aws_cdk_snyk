#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_snyk.aws_cdk_snyk_stack import AwsCdkSnykStack


app = cdk.App()
AwsCdkSnykStack(app, "aws-cdk-snyk")

app.synth()
