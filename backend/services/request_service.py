from datetime import datetime, timedelta
from models.vehicle import get_vehicle_by_type

DATE_FORMAT = "%Y-%m-%d %H:%M"


def validate_dates(request):
    is_valid = True
    request_date = datetime.strptime(request.request_date, DATE_FORMAT)
    start_date = datetime.strptime(request.appointment_date, DATE_FORMAT)
    end_date = start_date + timedelta(
        minutes=get_vehicle_by_type(request.vehicle_type).servicing_time
    )
    # Check if appointment date is after request date
    if start_date < request_date:
        is_valid = False

    # Check if appointment is exactly between 7am and 7pm
    if (
        start_date.hour < 7
        or (end_date.hour == 19 and end_date.minute > 0)
        or end_date.hour > 19
    ):
        is_valid = False

    return is_valid
