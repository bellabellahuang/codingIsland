## Snowflake      

### CLI Client     

### Installation      

        brew cask install snowflake-snowsql     

### Configuration      

        Set default login credentials in ~/.snowsql/config    

### Login      

        snowsql
        snowsql -c [template name in config file]  

### Run query directly

        snowsql -q "SELECT 100;"

### Run sql file

        snowsql -f query.sql

### Execution only

        -o execution_only=True

### SQL Scripts           

* [DATA IMPORT AND EXPORT](../scripts/snowflake/copy_into.sql)
* [MERGE TABLES](../scripts/snowflake/merge.sql)
* [IFF & CASE](../scripts/snowflake/iff_case.sql)
* [DATETIME](../scripts/snowflake/datetime.sql)

### Python connector        

[Connect to snowflake and excute queries](../scripts/snowflake/connector.py)       
