from vehicle import VehicleTypes, get_vehicle_by_type


class Request:
    def __init__(self, request_date, appointment_date, vehicle_type):
        self.request_date = request_date
        self.appointment_date = appointment_date
        self.vehicle: VehicleTypes = get_vehicle_by_type(vehicle_type)
