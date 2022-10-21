import snowflake.connector


def run(query):
    # Connect to snowflake
    connector = snowflake.connector.connect(
        user='username',
        password='password',
        account='account'
    )
    # run the query
    # https://docs.snowflake.com/en/user-guide/python-connector-example.html#binding-data
    cs = connector.cursor()
    try:
        cs.execute(query)
        results = cs.fetchall()
        for row in results:
            print(row[0])
    finally:
        cs.close()

    connector.close()
    return results
