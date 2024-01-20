class Request:
    def __init__(self, request_date, appointment_date, vehicle_type):
        self.request_date = request_date
        self.appointment_date = appointment_date
        self.vehicle_type = vehicle_type

    def display_info(self):
        print(f"Request Date: {self.request_date}")
        print(f"Appointment Date: {self.appointment_date}")
        print(f"Vehicle Type: {self.vehicle_type}")