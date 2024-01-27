import mysql.connector

from config.DBConnection import connect

# ======= Establishing Database Connection ===========
db_connection = connect()


class PartsService:

    # ===== This function is used to create new part =====
    def create_part(connection, data):
        try:
            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # SQL query to insert data into the table
            insert_query = "INSERT INTO your_table_name (id, title, make,part_number,brand,oem,aftermarket,part_condition," \
                           "description,compatibility_description,additional_info,listing_price,negotiable) VALUES (data, %s, %s)"

            # Execute the query with the data
            cursor.execute(insert_query, data)

            # Commit the changes to the database
            connection.commit()

            return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

        finally:
            # Close the cursor
            cursor.close()
