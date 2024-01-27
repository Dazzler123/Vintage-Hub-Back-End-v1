import mysql.connector
from configparser import ConfigParser


# Function to read the MySQL connection details from the configuration file
def read_db_config(filename='config.ini', section='mysql'):
    # Create a parser
    parser = ConfigParser()
    # Read the configuration file
    parser.read(filename)

    # Get the MySQL section
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(f"{section} not found in the {filename} file")

    return db


# Function to establish a connection to the MySQL server
def connect():
    try:
        # Read MySQL connection details from the configuration file
        db_config = read_db_config()

        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(**db_config)

        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
