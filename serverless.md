### Serverless

* refer to ssm parameters

        ${ssm:param-name}
        ${ssm:param-name~true} (use this for secure strings)

* GetAtt

        Fn::GetAtt  (Should be in a new line as the value, not the same line of the key)
        !GetAtt  (this formula works in cloudformation but not in serverless)

