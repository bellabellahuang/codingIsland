### AWS

* [install dependencies using lamda docker image](./aws/docker.md)

* Install aws-cli

        brew install aws-cli

* Delete all the files under a path in s3

        aws s3 rm s3://my-bucket/path --recursive

* Get the total size of a path in s3

        aws s3 ls --summarize --human-readable --recursive s3://bucket-name/

* Add a parameter to SSM

        aws ssm put-parameter --name "parameter_name" --value "parameter value" --type String/SecureString

* Update the parameter value in SSM

        aws ssm put-parameter --name “parameter_name” --value “parameter value” --type String/SecureString --overwrite

* Get the parameter value from SSM

        aws ssm get-parameters --names “parameter_name”




