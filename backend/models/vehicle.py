from enum import Enum


class VehicleTypes(Enum):
    COMPACT = ("compact", 30, 150)
    MEDIUM = ("medium", 30, 150)
    FULL_SIZE = ("full-size", 30, 150)
    CLASS_1_TRUCK = ("class 1 truck", 60, 250)
    CLASS_2_TRUCK = ("class 2 truck", 120, 700)

    def __init__(self, vehicle_type, servicing_time, charge):
        self.type = vehicle_type
        self.servicing_time = servicing_time
        self.charge = charge

    def __str__(self):
        return self.type


def get_vehicle_by_type(vehicle_type: str) -> "VehicleTypes":
    for vehicle in VehicleTypes:
        if vehicle.type == vehicle_type:
            return vehicle
    return None
