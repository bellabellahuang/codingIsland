### AWS

* [install dependencies using lamda docker image](../aws/docker.md)

* Install aws-cli

        brew install aws-cli

* Delete all the files under a path in s3

        aws s3 rm s3://my-bucket/path --recursive

* Get the total size of a path in s3

        aws s3 ls --summarize --human-readable --recursive s3://bucket-name/

* List all the objects under a path in s3

        aws s3 ls s3://{path} --recursive --human-readable

* Count the number of objects under a path in s3

        aws s3 ls --recursive s3://{path}/ | wc -l

* Add a parameter to SSM

        aws ssm put-parameter --name "parameter_name" --value "parameter value" --type String/SecureString

* Update the parameter value in SSM

        aws ssm put-parameter --name “parameter_name” --value “parameter value” --type String/SecureString --overwrite

* Get the parameter value from SSM

        aws ssm get-parameters --names “parameter_name”

* Download file from S3

        aws s3 cp s3://{BUCKET_NAME}/{FILE_PATH}/{FILE_NAME} ./Desktop/{LOCAL_FILE_NAME}

* Config Software MFA in cognito user pool

        aws cognito-idp set-user-pool-mfa-config --user-pool-id {USER_POOL_ID} --software-token-mfa-configuration Enabled=true --mfa-configuration ON

* Create a user in cognito user pool

        aws cognito-idp admin-create-user --user-pool-id {USER_POOL_ID} --username {USER_NAME} --temporary-password 000000




