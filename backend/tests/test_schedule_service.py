import pytest
import numpy as np
from app.services.schedule_service import (
    get_unique_days,
    get_requests_by_appointment_date,
    get_schedule_by_date,
    create_schedule_by_date,
)

DATE = "2022-10-01"


def test_get_unique_days():
    unique_days = get_unique_days
    assert len(unique_days) == len(set(unique_days))


def test_get_requests_by_appointment_date():
    requests = get_requests_by_appointment_date(DATE)
    assert np.all(requests["appointment_date"].str.contains(DATE))


def test_get_schedule_by_date():
    schedule = get_schedule_by_date(DATE)
    assert schedule.date == DATE


def test_create_schedule_by_date():
    schedule = create_schedule_by_date(DATE)
    assert schedule.date == DATE
