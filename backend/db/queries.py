import sqlite3

def drop_appointments_table(cursor: sqlite3.Cursor) -> None:
    query = '''
    DROP TABLE IF EXISTS appointments;
    '''
    cursor.execute(query)


def create_appointments_table(cursor: sqlite3. Cursor) -> None:
    query = '''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY,
        start_time DATETIME,
        car_type VARCHAR(50),
        end_time DATETIME
    );
    '''
    cursor.execute(query)


def add_appointment(cursor: sqlite3. Cursor, start_time, car_type, end_time) -> None:
    query = '''
    INSERT INTO appointments
    (start_time, car_type, end_time)
    VALUES (?, ?, ?);
    '''
    cursor.execute(query, (start_time, car_type, end_time))




