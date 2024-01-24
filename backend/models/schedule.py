from .bay import Bay
from .request import Request


class Schedule:
    def __init__(self, date):
        self.date = date
        self.profit = 0
        self.loss = 0
        self.bays = {
            Bay.COMPACT,
            Bay.MEDIUM,
            Bay.FULL_SIZE,
            Bay.CLASS_1_TRUCK,
            Bay.CLASS_2_TRUCK,
            Bay.FREE_STATION,
        }

    def add_appointment(self, request: Request):
        vehicle = request.vehicle
        for bay in self.bays:
            if bay.value == vehicle.type or bay.value == Bay.FREE_STATION.value:
                if bay.add_appointment(request):
                    self.profit += vehicle.charge
                    return True
        self.loss += vehicle.charge
        return False

    def to_dict(self):
        return {
            "date": self.date,
            "profit": self.profit,
            "loss": self.loss,
            "bays": [bay.to_dict() for bay in self.bays],
        }

    @classmethod
    def from_dict(cls, data):
        schedule = cls(data["date"])
        schedule.profit = data["profit"]
        schedule.loss = data["loss"]
        schedule.bays = [Bay.from_dict(bay) for bay in data["bays"]]
        return schedule
