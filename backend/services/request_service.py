from datetime import datetime


class RequestValidation:
    def __init__(self, request):
        self.request = request
        self.valid = True
        self.error_message = ""

    def validate_dates(self):
        # Check if dates are valid format
        try:
            request_date = datetime.strptime(
                self.request.request_date, "%Y-%m-%d %H:%M:%S"
            )
            appointment_date = datetime.strptime(
                self.request.appointment_date, "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            self.valid = False
            self.error_message = "Invalid date format"
            return

        # Check if appointment date is after request date and in the future
        if appointment_date <= request_date or appointment_date <= datetime.now():
            self.valid = False
            self.error_message = (
                "Appointment date must be after request date and in the future"
            )
            return

        # Check if date is between 7am and 7pm and in October or November
        if not (
            7 <= appointment_date.hour <= 19 and appointment_date.month in [10, 11]
        ):
            self.valid = False
            self.error_message = "Appointment date must be between 7am and 7pm and in October or November"
