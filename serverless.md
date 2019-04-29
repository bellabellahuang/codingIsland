### Serverless

* [my serverless template](./scripts/sls-template.yml)

* refer to ssm parameters

        ${ssm:param-name}
        ${ssm:param-name~true} (use this for secure strings)

* GetAtt

        Fn::GetAtt  (Should be in a new line as the value, not the same line of the key)
        !GetAtt  (this formula works in cloudformation but not in serverless)

* deployment with existing bucket

        deploymentBucket  (in provider)

* api gateway should be declared in provider if a callback url is needed in functions, in this case, it is created according to the customized settings in resources section instead of created by aws in deployment

        apiGateway  (in provider)

* configure the number of messages to be processed in one event at a time

        batchSize  (in functions)

* configure the number of triggered functions to work at the same time

        reservedConcurrency  (in functions)

* [configure cloudwatch schedule events for Lambda functions](https://serverless.com/framework/docs/providers/aws/events/schedule/)

        schedule: rate(10 minutes)
        schedule: cron(*/10 * * * *)
