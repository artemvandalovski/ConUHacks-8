from datetime import date, datetime
import sqlite3

from backend.db.create_tables import create_tables
from backend.db.db import connect, disconnect
from backend.db.helpers import get_appointments_by_date
from backend.db.queries import add_appointment, select_appointments_by_date

config_path = 'config/project_config.json'
create_tables(config_path)

connection, cursor = connect(config_path)

appointment_data = {
    'start_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'car_type': 'Sedan',
    'end_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
}
add_appointment(cursor, connection, appointment_data['start_time'], appointment_data['car_type'], appointment_data['end_time'])


sdates = [
    datetime(2024, 1, 20, 12, 0, 0),
    datetime(2024, 1, 19, 12, 0, 0),
    datetime(2024, 1, 18, 12, 0, 0),
    datetime(2024, 1, 19, 8, 0, 0),
    datetime(2024, 1, 19, 11, 0, 0),
    datetime(2024, 1, 18, 12, 0, 0),
]
edates = [
    datetime(2024, 1, 20, 12, 0, 0),
    datetime(2024, 1, 19, 15, 0, 0),
    datetime(2024, 1, 18, 12, 0, 0),
    datetime(2024, 1, 19, 16, 0, 0),
    datetime(2024, 1, 19, 17, 0, 0),
    datetime(2024, 1, 18, 12, 0, 0),
]
types = [
    'Toyota',
    'c1',
    'Mazda',
    'c2',
    'c3',
    'Porsche',
]

for d1, d2, t in zip(sdates, edates, types):
    add_appointment(cursor, connection, d1, t, d2)

for ct, sd, ed in get_appointments_by_date(cursor, date(2024, 1, 19)):
    print(f'[{ct}]: From {sd} to {ed}')

disconnect(connection, cursor)

