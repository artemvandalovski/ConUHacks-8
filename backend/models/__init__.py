from datetime import datetime, timedelta
from enum import Enum

DATE_FORMAT = "%Y-%m-%d %H:%M"
to_date = lambda date: datetime.strptime(date, DATE_FORMAT)
from_date = lambda date: datetime.strftime(date, DATE_FORMAT)
