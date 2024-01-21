import sqlite3

from backend.db.db import connect, disconnect
from backend.db.queries import create_appointments_table, create_quotas_table, drop_appointments_table, drop_quotas_table


def create_tables(config_path: str) -> None:
    try:
        # Establish a connection to the database
        connection, cursor = connect(config_path)

        # Drop tables if they exist
        drop_appointments_table(cursor)
        drop_quotas_table(cursor)

        # Create a new table
        create_appointments_table(cursor)
        create_quotas_table(cursor)
        
        # Commit the changes
        connection.commit()
    
    # Catch error
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    # Close the connection
    finally:
        print('Table created')
        disconnect(connection, cursor)
