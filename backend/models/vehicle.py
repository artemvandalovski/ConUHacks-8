class Vehicle:
    def __init__(self, vehicle_type, servicing_time, charge):
        self.vehicle_type = vehicle_type
        self.servicing_time = servicing_time
        self.charge = charge


VEHICLES = [
    Vehicle("compact", 30, 150),
    Vehicle("medium", 30, 150),
    Vehicle("full-size", 30, 150),
    Vehicle("class 1 truck", 60, 250),
    Vehicle("class 2 truck", 120, 700),
]


def get_vehicle_by_type(vehicle_type):
    for vehicle in VEHICLES:
        if vehicle.vehicle_type == vehicle_type:
            return vehicle
