from datetime import date, datetime
import sqlite3
from typing import List, Tuple

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


def add_appointment(cursor: sqlite3. Cursor, connection: sqlite3.Connection, start_time: datetime, car_type: str, end_time: datetime) -> None:
    '''
    Add a new appointment to the `appointments` table.

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
    connection.commit()


def select_appointments_by_date(cursor: sqlite3.Cursor, target_date: date) -> List[Tuple[int, str, str, str]]:
    '''
    Fetch all appointments for a given date from the `appointments` table.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor object.
    - target_date (date): The target date to fetch appointments.

    Returns:
    List[Tuple[int, str, str, str]]: A list of tuples representing appointments.
    '''
    query = '''
    SELECT * FROM appointments
    WHERE DATE(start_time) = ?;
    '''

    # Convert the target_date to a string in the 'YYYY-MM-DD' format
    target_date_str = target_date.strftime('%Y-%m-%d')

    # Execute the query with the target_date parameter
    cursor.execute(query, (target_date_str,))

    # Fetch all rows
    appointments = cursor.fetchall()

    return appointments



