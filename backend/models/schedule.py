from datetime import datetime, timedelta
from models.vehicle import get_vehicle_by_type


class Request:
    def __init__(self, request_date, appointment_date, vehicle_type):
        self.request_date = request_date
        self.appointment_date = appointment_date
        self.vehicle_type = vehicle_type


class Schedule:
    def __init__(self, date):
        self.date = date
        self.schedule = {}

    def is_slot_available(self, date, vehicle):
        start_time = datetime.strptime(date, "%Y-%m-%d %H:%M")
        end_time = start_time + timedelta(minutes=vehicle.servicing_time)
        for appointment in self.schedule.values():
            appointment_start_time = datetime.strptime(
                appointment.appointment_date, "%Y-%m-%d %H:%M"
            )
            appointment_end_time = appointment_start_time + timedelta(
                minutes=get_vehicle_by_type(appointment.vehicle_type).servicing_time
            )
            if (
                start_time <= appointment_start_time
                and end_time >= appointment_start_time
            ) or (
                start_time >= appointment_start_time
                and start_time <= appointment_end_time
            ):
                return False

    def add_appointment(self, request):
        self.schedule[request.request_date] = request
        print("added" + request.request_date)
