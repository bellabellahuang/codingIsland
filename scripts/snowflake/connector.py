import snowflake.connector


def run(query):
    # Connect to snowflake
    connector = snowflake.connector.connect(
        user='username',
        password='password',
        account='account'
    )
    # run the query
    cs = connector.cursor()
    try:
        cs.execute(query)
        results = cs.fetchall()
    finally:
        cs.close()

    connector.close()
    return results
