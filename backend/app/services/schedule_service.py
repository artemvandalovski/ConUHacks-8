from . import df, get_unique_days
from models.request import Request
from models.schedule import Schedule
from repo.schedule_repo import get_schedule, save_schedule
from .request_service import validate_request


def get_requests_by_appointment_date(date):
    return df.loc[df["appointment_date"].str.contains(date)]


def get_schedule_by_date(date):
    schedule = get_schedule(date)
    if schedule is None:
        schedule = create_schedule_by_date(date)
    return schedule


def create_schedule_by_date(date):
    schedule = Schedule(date)
    requests = get_requests_by_appointment_date(date)
    for _, request in requests.iterrows():
        request = Request.from_csv(request)
        if validate_request(request):
            schedule.add_appointment(request)
    save_schedule(schedule)
    return schedule


def create_all_schedules():
    for date in get_unique_days:
        create_schedule_by_date(str(date))
