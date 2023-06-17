import pytest
import mysql.connector
from pytestproject.math import add

def get_test_data_from_mysql():
    # Establish a connection to your MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    # Execute a query to retrieve test data from a table
    cursor = conn.cursor()
    query = "SELECT a, b, expected FROM test_data_table"
    cursor.execute(query)

    # Fetch all rows of the result set
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    return rows

class MathOperationsTest:
    @pytest.mark.parametrize("a, b, expected", get_test_data_from_mysql())
    def test_add(self, a, b, expected):
        result = add(a, b)
        assert result == expected
