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
            # print(f"Appointment for {vehicle.type} at {date} is not available")
            return False
        self.schedule.append(
            Appointment(
                start_time.strftime(DATE_FORMAT),
                end_time.strftime(DATE_FORMAT),
                vehicle.type,
            )
        )
        # print(f"Added appointment for {vehicle.type} at {date}")
        return True

    def to_dict(self):
        return {
            "schedule": self.schedule,
        }

    @classmethod
    def from_dict(cls, bay_dict):
        bay = cls()
        bay.schedule = bay_dict["schedule"]
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
            if bay == vehicle.type:  # TODO: add logic for free stations
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
            "bays": {
                "compact": self.bays["compact"].to_dict(),
                "medium": self.bays["medium"].to_dict(),
                "full-size": self.bays["full-size"].to_dict(),
                "class 1 truck": self.bays["class 1 truck"].to_dict(),
                "class 2 truck": self.bays["class 2 truck"].to_dict(),
                "free station 1": self.bays["free station 1"].to_dict(),
                "free station 2": self.bays["free station 2"].to_dict(),
                "free station 3": self.bays["free station 3"].to_dict(),
                "free station 4": self.bays["free station 4"].to_dict(),
                "free station 5": self.bays["free station 5"].to_dict(),
            },
        }

    @classmethod
    def from_dict(cls, schedule_dict):
        schedule = cls(schedule_dict["date"])
        schedule.profit = schedule_dict["profit"]
        schedule.loss = schedule_dict["loss"]
        schedule.bays = {
            "compact": Bay.from_dict(schedule_dict["bays"]["compact"]),
            "medium": Bay.from_dict(schedule_dict["bays"]["medium"]),
            "full-size": Bay.from_dict(schedule_dict["bays"]["full-size"]),
            "class 1 truck": Bay.from_dict(schedule_dict["bays"]["class 1 truck"]),
            "class 2 truck": Bay.from_dict(schedule_dict["bays"]["class 2 truck"]),
            "free station 1": Bay.from_dict(schedule_dict["bays"]["free station 1"]),
            "free station 2": Bay.from_dict(schedule_dict["bays"]["free station 2"]),
            "free station 3": Bay.from_dict(schedule_dict["bays"]["free station 3"]),
            "free station 4": Bay.from_dict(schedule_dict["bays"]["free station 4"]),
            "free station 5": Bay.from_dict(schedule_dict["bays"]["free station 5"]),
        }
        return schedule
