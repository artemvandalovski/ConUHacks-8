class Vehicle:
    def __init__(self, vehicle_type, servicing_time, charge):
        self.type = vehicle_type
        self.servicing_time = servicing_time
        self.charge = charge

    def to_dict(self):
        return {
            "type": self.type,
            "servicing_time": self.servicing_time,
            "charge": self.charge,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


VEHICLES = [
    Vehicle("compact", 30, 150),
    Vehicle("medium", 30, 150),
    Vehicle("full-size", 30, 150),
    Vehicle("class 1 truck", 60, 250),
    Vehicle("class 2 truck", 120, 700),
]


def get_vehicle_by_type(vehicle_type):
    for vehicle in VEHICLES:
        if vehicle.type == vehicle_type:
            return vehicle
