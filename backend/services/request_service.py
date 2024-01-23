from datetime import datetime, timedelta
from models.vehicle import get_vehicle_by_type

DATE_FORMAT = "%Y-%m-%d %H:%M"


def validate_dates(request):
    request_date = datetime.strptime(request.request_date, DATE_FORMAT)
    start_date = datetime.strptime(request.appointment_date, DATE_FORMAT)
    end_date = start_date + timedelta(
        minutes=get_vehicle_by_type(request.vehicle_type).servicing_time
    )

    is_valid = (
        start_date >= request_date and 7 <= start_date.hour < 19 and end_date.hour <= 19
    )

    return is_valid
