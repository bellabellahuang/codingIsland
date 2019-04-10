### Installing dependecies in AWS environment

in the project working directory
> $ mkdir .vendor
>
> $ docker run -v "$PWD":/var/task -it lambci/lambda:build-python3.6 bash
>
> $ pip install snowflake-connector-python
>
> $ pip freeze > requirements.txt
>
> $ pip install -r requirements.txt -t .vendor

in the serverless.yml

    package
      include:
        - .vendor/**

in handler.py
      
    import sys
    sys.path.insert(0, './.vendor')
    import snowflake.connector


* [docker reference](https://pedoublety.wordpress.com/2017/06/22/building-python-packages-for-aws-lambda/
)

* [vendor reference](https://stackoverflow.com/questions/36944330/how-do-i-deploy-a-function-in-python-with-its-dependencies/41634501#41634501
)