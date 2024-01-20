from models.vehicle import get_vehicle_by_type
from datetime import datetime, timedelta


class Request:
    def __init__(self, request_date, appointment_date, vehicle_type):
        self.request_date = request_date
        self.appointment_date = appointment_date
        self.vehicle_type = vehicle_type


class Schedule:
    def __init__(self, date):
        self.date = date
        self.schedules = {}
        self.profit = 0
        self.loss = 0

    def add_appointment(self, request):
        if not self.is_slot_available(request):
            return False
        self.schedule[request.appointment_date] = request
        return True

    def is_slot_available(self, request):
        vehicle = get_vehicle_by_type(request.vehicle_type)
        if not vehicle:
            return False
        start_time = datetime.strptime(request.appointment_date, "%Y-%m-%d %H:%M")
        end_time = start_time + timedelta(minutes=vehicle.servicing_time)
        for appointment in self.schedule.values():
            appointment_start_time = datetime.strptime(
                appointment.appointment_date, "%Y-%m-%d %H:%M"
            )
            appointment_end_time = appointment_start_time + timedelta(
                minutes=vehicle.servicing_time
            )
            if (
                start_time <= appointment_start_time
                and end_time >= appointment_start_time
            ) or (
                start_time >= appointment_start_time
                and start_time <= appointment_end_time
            ):
                return False
