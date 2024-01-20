from backend.db.queries import select_appointments_by_date

from datetime import date, datetime, time
import sqlite3
from typing import List, Tuple

def get_appointments_by_date(cursor: sqlite3.Cursor, target_date: date) -> List[Tuple[str, time, time]]:
    '''
    Extracts relevant information from a list of appointments.

    Parameters:
    - appointments (List[Tuple[int, str, str, str]]): A list of appointments represented as tuples.
      Each tuple contains (id, start_time, car_type, end_time).

    Returns:
    List[Tuple[str, time, time]]: A list of tuples containing extracted information.
      Each tuple contains (car_type, start_time, end_time).
      - car_type (str): The type of car for the appointment.
      - start_time (time): The start time of the appointment (extracted from 'start_time' string).
      - end_time (time): The end time of the appointment (extracted from 'end_time' string).
    '''
    appointments = select_appointments_by_date(cursor, target_date)
    
    def get_time_from_str(date_str):
        to_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return to_date.time()
    
    return [(car_type, get_time_from_str(start_time), get_time_from_str(end_time)) for _, start_time, car_type, end_time in appointments]
