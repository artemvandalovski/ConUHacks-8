from datetime import datetime, timedelta
from models.request import Request

DATE_FORMAT = "%Y-%m-%d %H:%M"


def validate_request(request: Request):
    vehicle = request.vehicle
    request_date = request.request_date
    start_date = request.appointment_date
    end_date = start_date + timedelta(minutes=vehicle.servicing_time)

    is_valid = (
        start_date >= request_date and 7 <= start_date.hour < 19 and end_date.hour <= 19
    )

    return is_valid
