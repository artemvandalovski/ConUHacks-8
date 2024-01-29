import pandas as pd
from datetime import datetime as dt, timedelta as td

df = pd.read_csv(
    "utils/datafile.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)

DATE_FORMAT = "%Y-%m-%d %H:%M"
to_date = lambda date: dt.strptime(date, DATE_FORMAT)
from_date = lambda date: dt.strftime(date, DATE_FORMAT)
get_unique_days = pd.to_datetime(df["appointment_date"]).dt.date.unique()
