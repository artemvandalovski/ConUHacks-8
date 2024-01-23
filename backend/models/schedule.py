from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d %H:%M"


class Appointment:
    def __init__(self, start_time, end_time, vehicle):
        self.start_time = start_time
        self.end_time = end_time
        self.vehicle = vehicle

    def to_dict(self):
        return {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "vehicle": self.vehicle.to_dict(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


class Bay:
    def __init__(self):
        self.appointments = []

    def is_slot_available(self, start_time, end_time):
        for appointment in self.appointments:
            appointment_start_time = datetime.strptime(
                appointment.start_time, DATE_FORMAT
            )
            appointment_end_time = datetime.strptime(appointment.end_time, DATE_FORMAT)
            if (
                start_time >= appointment_start_time
                and start_time <= appointment_end_time
            ) or (
                end_time >= appointment_start_time and end_time <= appointment_end_time
            ):
                return False
        return True

    def add_appointment(self, date, vehicle):
        start_time = datetime.strptime(date, DATE_FORMAT)
        end_time = start_time + timedelta(minutes=vehicle.servicing_time)
        if not self.is_slot_available(start_time, end_time):
            return False
        self.appointments.append(
            Appointment(
                start_time.strftime(DATE_FORMAT),
                end_time.strftime(DATE_FORMAT),
                vehicle,
            )
        )
        return True

    def to_dict(self):
        return {
            "appointments": [appointment.to_dict() for appointment in self.appointments]
        }

    @classmethod
    def from_dict(cls, data):
        bay = cls()
        bay.appointments = [
            Appointment.from_dict(appointment) for appointment in data["appointments"]
        ]
        return bay


class Schedule:
    def __init__(self, date):
        self.date = date
        self.profit = 0
        self.loss = 0
        self.bays = {
            "compact": Bay(),
            "medium": Bay(),
            "full-size": Bay(),
            "class 1 truck": Bay(),
            "class 2 truck": Bay(),
            "free station 1": Bay(),
            "free station 2": Bay(),
            "free station 3": Bay(),
            "free station 4": Bay(),
            "free station 5": Bay(),
        }

    def add_appointment(self, date, vehicle):
        for bay in self.bays:
            if vehicle.type == bay:  # TODO: add logic for free stations
                if self.bays[bay].add_appointment(date, vehicle):
                    self.profit += vehicle.charge
                    return True
        self.loss += vehicle.charge
        return False

    def to_dict(self):
        return {
            "date": self.date,
            "profit": self.profit,
            "loss": self.loss,
            "bays": {bay: self.bays[bay].to_dict() for bay in self.bays},
        }

    @classmethod
    def from_dict(cls, data):
        schedule = cls(data["date"])
        schedule.profit = data["profit"]
        schedule.loss = data["loss"]
        schedule.bays = {bay: Bay.from_dict(data["bays"][bay]) for bay in data["bays"]}
        return schedule
