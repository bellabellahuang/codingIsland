### Bash

* executes the content of the file passed as argument

        source env.sh
        . env.sh

* updates file permissions

        chmod 0600 file

* output the first line of a file

        head -1 file

* output the number of files in a directory

        ls -1 | wc -l

* search keywords in the output

        aws s3 ls s3://bucket-name//path//.. | grep keyword_1 | grep keyword_2
