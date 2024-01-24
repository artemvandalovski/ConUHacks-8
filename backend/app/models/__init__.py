from datetime import datetime as dt, timedelta as td
from enum import Enum

DATE_FORMAT = "%Y-%m-%d %H:%M"
to_date = lambda date: dt.strptime(date, DATE_FORMAT)
from_date = lambda date: dt.strftime(date, DATE_FORMAT)
