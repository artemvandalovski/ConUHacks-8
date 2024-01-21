import pandas as pd
from models.schedule import Schedule
from models.vehicle import get_vehicle_by_type

df = pd.read_csv(
    "resources/test.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)


def filter_by_appointment_date(date):
    return df.loc[df["appointment_date"].str.contains(date)]


def load_schedule(date):
    schedule = Schedule(date)

    requests_by_date = filter_by_appointment_date(date)
    requests_by_date.sort_values(by="request_date")

    for _, request in requests_by_date.iterrows():
        vehicle = get_vehicle_by_type(request.vehicle_type)
        schedule.add_appointment(request.appointment_date, vehicle)
