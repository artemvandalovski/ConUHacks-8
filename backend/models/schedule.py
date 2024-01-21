from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d %H:%M"


class Request:
    def __init__(self, request_date, appointment_date, vehicle_type):
        self.request_date = request_date
        self.appointment_date = appointment_date
        self.vehicle_type = vehicle_type


class Appointment:
    def __init__(self, start_time, end_time, vehicle):
        self.start_time = start_time
        self.end_time = end_time
        self.vehicle = vehicle


class Bay:
    def __init__(self):
        self.schedule = []

    def is_slot_available(self, start_time, end_time):
        for appointment in self.schedule:
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
            print(f"Appointment for {vehicle.type} at {date} is not available")
            return False
        self.schedule.append(
            Appointment(
                start_time.strftime(DATE_FORMAT),
                end_time.strftime(DATE_FORMAT),
                vehicle.type,
            )
        )
        print(f"Added appointment for {vehicle.type} at {date}")
        return True


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
        }

    def add_appointment(self, date, vehicle):
        for bay in self.bays:
            if bay == "any" or bay == vehicle.type:
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
            "bays": {key: value.to_dict() for key, value in self.bays.items()},
        }

    @classmethod
    def from_dict(cls, data):
        schedule = cls(date=data["date"])
        schedule.profit = data["profit"]
        schedule.loss = data["loss"]
        for key, value in data["bays"].items():
            schedule.bays[key] = Bay.from_dict(value)
        return schedule
