import pandas as pd
from models.schedule import Schedule
from models.vehicle import get_vehicle_by_type
from services.request_service import validate_dates
from repo.schedule_repo import get_schedule, save_schedule

df = pd.read_csv(
    "../resources/datafile.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)


def filter_by_appointment_date(date):
    return df.loc[df["appointment_date"].str.contains(date)]


def create_schedule_by_date(date):
    schedule = Schedule(date)

    requests_by_date = filter_by_appointment_date(date)
    requests_by_date.sort_values(by="request_date")
    requests_by_date = requests_by_date[requests_by_date.apply(validate_dates, axis=1)]

    for _, request in requests_by_date.iterrows():
        vehicle = get_vehicle_by_type(request.vehicle_type)
        schedule.add_appointment(request.appointment_date, vehicle)

    save_schedule(schedule)
    return schedule


def get_schedule_by_date(date):
    schedule = get_schedule(date)
    if schedule is None:
        schedule = create_schedule_by_date(date)
    return schedule
