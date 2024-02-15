import pyodbc

# drivers = pyodbc.drivers()
# print(f"Available drivers:")
# for driver in drivers:
#     print(driver)

driver_name = "{ODBC Driver 17 for SQL Server}"

server_name = "DESKTOP-7CB1RAA"
database_name = "master"
username = "your_username"
password = "your_password"

use_windows_auth = True

# conn = pyodbc.connect(
#     '''
#     DRIVER={ODBC Driver 17 for SQL Server};
#     SERVER=DESKTOP-7CB1RAA;
#     DATABASE=master;
#     Trusted_Connection=yes;
#     '''
#     )

try:
    # Build the connection string
    if use_windows_auth:
        conn_str = (
            f"DRIVER={driver_name};"
            f"SERVER={server_name};"
            f"DATABASE={database_name};"
            f"Trusted_Connection=yes;"
        )
    else:
        conn_str = (
            f"DRIVER={driver_name};"
            f"SERVER={server_name};"
            f"DATABASE={database_name};"
            f"UID={username};"
            f"PWD={password};"
        )

    # Create the connection
    conn = pyodbc.connect(conn_str)

    # Execute a simple query to test the connection

    cursor = conn.cursor()

    cursor.execute("SELECT 1 AS test_value")
    result = cursor.fetchone()

    if result[0] == 1:
        print("Connection successful!")
    else:
        print("Unexpected query result.")

except pyodbc.Error as ex:
    print("Error connecting to database:", ex)

finally:
    # Close the connection if opened
    if conn:
        conn.close()

    