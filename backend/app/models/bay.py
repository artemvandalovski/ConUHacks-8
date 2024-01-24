from . import Enum
from .appointment import Appointment
from .request import Request


class Bay(Enum):
    COMPACT = "compact"
    MEDIUM = "medium"
    FULL_SIZE = "full-size"
    CLASS_1_TRUCK = "class 1 truck"
    CLASS_2_TRUCK = "class 2 truck"
    FREE_STATION = "any"

    def __init__(self, bay_type):
        self.bay_type = bay_type
        self.appointments: list[Appointment] = []

    def is_slot_available(self, start_time, end_time):
        for appointment in self.appointments:
            app_start, app_end = appointment.start_time, appointment.end_time
            if (app_start <= start_time < app_end) or (app_start < end_time <= app_end):
                return False
        return True

    def add_appointment(self, request: Request):
        appointment = Appointment(request)
        if self.is_slot_available(appointment.start_time, appointment.end_time):
            self.appointments.append(appointment)
            return True
        return False

    def to_dict(self):
        return [appointment.to_dict() for appointment in self.appointments]

    @classmethod
    def from_dict(cls, data):
        return cls([Appointment.from_dict(appointment) for appointment in data])
