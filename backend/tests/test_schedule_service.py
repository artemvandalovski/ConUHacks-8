import pytest
from app.services.schedule_service import (
    get_requests_by_appointment_date,
    get_schedule_by_date,
    create_schedule_by_date,
)


def test_get_requests_by_appointment_date():
    appointment_date = "2022-10-01"
    requests = get_requests_by_appointment_date(appointment_date)
    assert len(requests) > 0


def test_get_schedule_by_date():
    date = "2022-10-01"
    schedule = get_schedule_by_date(date)
    assert schedule.date == date


def test_create_schedule_by_date():
    date = "2022-10-01"
    schedule = create_schedule_by_date(date)
    assert schedule.date == date
