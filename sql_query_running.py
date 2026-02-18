import pyodbc


def run_sql_query_for_validation(sql_query_to_be_run):
    # Move connection details here to ensure they are fresh for every test
    conn_str = (
        "Driver={ODBC Driver 18 for SQL Server};"
        r"Server=127.0.0.1,1433;"
        "Database=AdventureWorksDW_3;"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    # The 'with' block acts as a Context Manager
    # It keeps the connection open for the duration of the indented code
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            print("===========================================")
            print(f"Running requested query : {sql_query_to_be_run}")
            print("-------------------------------------------")
            cursor.execute(sql_query_to_be_run)
            data = cursor.fetchall()
            print("End of the query")
            return data