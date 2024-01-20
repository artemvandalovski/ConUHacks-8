from datetime import datetime
import sqlite3

from backend.db.create_tables import create_tables
from backend.db.db import connect, disconnect
from backend.db.queries import add_appointment

config_path = 'config/project_config.json'
create_tables(config_path)

connection, cursor = connect(config_path)

appointment_data = {
    "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "car_type": "Sedan",
    "end_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}
add_appointment(cursor, appointment_data["start_time"], appointment_data["car_type"], appointment_data["end_time"])
connection.commit()

disconnect(connection, cursor)

