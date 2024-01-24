from . import Enum


class Vehicle(Enum):
    COMPACT = ("compact", 30, 150)
    MEDIUM = ("medium", 30, 150)
    FULL_SIZE = ("full-size", 30, 150)
    CLASS_1_TRUCK = ("class 1 truck", 60, 250)
    CLASS_2_TRUCK = ("class 2 truck", 120, 700)

    def __init__(self, vehicle_type, servicing_time, charge):
        self.type = vehicle_type
        self.servicing_time = servicing_time
        self.charge = charge

    @staticmethod
    def get_vehicle_by_type(vehicle_type: str):
        for vehicle in Vehicle:
            if vehicle.type == vehicle_type:
                return vehicle
        return None

    def to_dict(self):
        return {
            "vehicle_type": self.type,
            "servicing_time": self.servicing_time,
            "charge": self.charge,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["vehicle_type"],
            data["servicing_time"],
            data["charge"],
        )
