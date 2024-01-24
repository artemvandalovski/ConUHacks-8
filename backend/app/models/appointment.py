from . import td, to_date, from_date
from .request import Request
from .vehicle import Vehicle


class Appointment:
    def __init__(self, request: Request):
        self.vehicle = request.vehicle
        self.start_time = request.appointment_date
        self.end_time = self.start_time + td(minutes=self.vehicle.servicing_time)

    def to_dict(self):
        return {
            "start_time": from_date(self.start_time),
            "end_time": from_date(self.end_time),
            "vehicle": self.vehicle.to_dict(),
        }

    @classmethod
    def from_dict(cls, data):
        appointment = cls(
            to_date(data["start_time"]), Vehicle.from_dict(data["vehicle"])
        )
        appointment.end_time = to_date(data["end_time"])
        return appointment
