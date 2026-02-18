import pyodbc

# Bypasses the "Name" entirely using IP and Port
# Note: Ensure Port 1433 is enabled in Configuration Manager first
SERVER_NAME = "127.0.0.1,1433"
DATABASE_NAME = "AdventureWorksDW_3"

connection_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    f"Server={SERVER_NAME};"
    f"Database={DATABASE_NAME};"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")