from backend.db.queries import select_appointments_by_date

from datetime import date, datetime
from typing import List, Tuple

def get_appointments_by_date(appointments: List[Tuple[int, str, str, str]]):
    return [(car_type, datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').time(), datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S').time()) for _, start_time, car_type, end_time in appointments]