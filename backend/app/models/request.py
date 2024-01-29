from . import to_date, dt
from .vehicle import Vehicle


class Request:
    def __init__(self, request_date, appointment_date, vehicle_type):
        self.request_date: dt = to_date(request_date)
        self.appointment_date: dt = to_date(appointment_date)
        self.vehicle: Vehicle = Vehicle.get_vehicle_by_type(vehicle_type)

    def to_dict(self):
        return {
            "request_date": self.request_date,
            "appointment_date": self.appointment_date,
            "vehicle": self.vehicle.to_dict(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["request_date"],
            data["appointment_date"],
            data["vehicle"]["type"],
        )

    @classmethod
    def from_csv(cls, data):
        return cls(
            data["request_date"],
            data["appointment_date"],
            data["vehicle_type"],
        )
