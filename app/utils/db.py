import os
import mysql.connector

def get_mysql_time():
    """Connect to MySQL and fetch CURRENT_TIMESTAMP."""
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "my-mysql"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "my-secret-pw"),
        database=os.getenv("MYSQL_DB", "mysql")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_TIMESTAMP();")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0]