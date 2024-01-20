from enum import Enum, auto


class VehicleType(Enum):
    COMPACT_CAR = auto()
    MEDIUM_CAR = auto()
    FULL_SIZE_CAR = auto()
    CLASS_1_TRUCK = auto()
    CLASS_2_TRUCK = auto()


class Vehicle:
    def __init__(self):
        self.servicing_times = {
            VehicleType.COMPACT_CAR: 30,
            VehicleType.MEDIUM_CAR: 30,
            VehicleType.FULL_SIZE_CAR: 30,
            VehicleType.CLASS_1_TRUCK: 60,
            VehicleType.CLASS_2_TRUCK: 120,
        }

        self.service_charges = {
            VehicleType.COMPACT_CAR: 150,
            VehicleType.MEDIUM_CAR: 150,
            VehicleType.FULL_SIZE_CAR: 150,
            VehicleType.CLASS_1_TRUCK: 250,
            VehicleType.CLASS_2_TRUCK: 700,
        }

    def get_servicing_time(self, vehicle_type):
        return self.servicing_times.get(vehicle_type, 0)

    def get_service_charge(self, vehicle_type):
        return self.service_charges.get(vehicle_type, 0)
