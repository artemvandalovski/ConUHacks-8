import sqlite3

def drop_appointments_table(cursor: sqlite3.Cursor) -> None:
    '''
    Drop the `appointments` table if it exists.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor object.

    Returns:
    None
    '''
    query = '''
    DROP TABLE IF EXISTS appointments;
    '''
    cursor.execute(query)


def create_appointments_table(cursor: sqlite3. Cursor) -> None:
    '''
    Create the `appointments` table if it doesn't exist.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor object.

    Returns:
    None
    '''
    query = '''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY,
        start_time DATETIME,
        car_type VARCHAR(50),
        end_time DATETIME
    );
    '''
    cursor.execute(query)

def drop_quotas_table(cursor: sqlite3.Cursor) -> None:
    '''
    Drop the `quotas` table if it exists.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor object.

    Returns:
    None
    '''
    query = '''
    DROP TABLE IF EXISTS quotas;
    '''
    cursor.execute(query)


def create_quotas_table(cursor: sqlite3. Cursor) -> None:
    '''
    Create the `quotas` table if it doesn't exist.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor object.

    Returns:
    None
    '''
    query = '''
    CREATE TABLE IF NOT EXISTS quotas (
        id INTEGER PRIMARY KEY,
        profits INTEGER,
        losses INTEGER,
        date DATETIME
    );
    '''
    cursor.execute(query)


def add_appointment(cursor: sqlite3. Cursor, start_time, car_type, end_time) -> None:
    '''
    Add a new appointment to the 'appointments' table.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor object.
    - start_time: The start time of the appointment.
    - car_type: The type of car for the appointment.
    - end_time: The end time of the appointment.

    Returns:
    None
    '''
    query = '''
    INSERT INTO appointments
    (start_time, car_type, end_time)
    VALUES (?, ?, ?);
    '''
    cursor.execute(query, (start_time, car_type, end_time))
