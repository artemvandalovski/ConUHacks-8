import pandas as pd
import models.vehicle as vehicle
from datetime import datetime, timedelta


class TireChangeShopScheduler:
    def __init__(self, start_time, end_time):
        self.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        self.end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        self.available_bays = {
            "Compact": [],
            "Medium": [],
            "Full-Size": [],
            "Class 1": [],
            "Class 2": [],
        }
        self.revenue = 0
        self.revenue_loss = 0
        self.served_customers = {key: 0 for key in self.available_bays.keys()}
        self.turn_away_customers = {key: 0 for key in self.available_bays.keys()}


df = pd.read_csv(
    "datafile.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)
df.head()

df.sort_values(by=["request_date"], inplace=True)

schedule = {}

for index, row in df.iterrows():
    #     check if the appointment date is before the request date
    if row["appointment_date"] < row["request_date"]:
        continue
