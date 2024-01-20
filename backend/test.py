import pandas as pd
from models.schedule import Schedule

# validate request
# is slot available
# 5 free bays and 1 bay for each vehicle type
# calculate losses

TODAY = "2022-10-04"

profit = 0
loss = 0

df = pd.read_csv(
    "resources/datafile.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)


def filter_by_appointment_date(date):
    return df.loc[df["appointment_date"].str.contains(date)]


def load_schedule(date):
    schedule = {}
    requests_by_date = filter_by_appointment_date(date)
    requests_by_date.sort_values(by="request_date")

    for index, request in requests_by_date.iterrows():
        pass


# load_schedule(TODAY)

Schedule(TODAY)
