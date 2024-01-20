class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.servicing_time = 0
        self.charge = 0

    def set_servicing_time(self, servicing_time):
        self.servicing_time = servicing_time

    def set_charge(self, charge):
        self.charge = charge

    def display_info(self):
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Servicing Time: {self.servicing_time} minutes")
        print(f"Charge: ${self.charge}")


class CompactCar(Vehicle):
    def __init__(self):
        super().__init__("Compact Car")
        self.set_servicing_time(30)
        self.set_charge(150)


class MediumCar(Vehicle):
    def __init__(self):
        super().__init__("Medium Car")
        self.set_servicing_time(30)
        self.set_charge(150)


class FullSizeCar(Vehicle):
    def __init__(self):
        super().__init__("Full-Size Car")
        self.set_servicing_time(30)
        self.set_charge(150)


class Class1Truck(Vehicle):
    def __init__(self):
        super().__init__("Class 1 Truck")
        self.set_servicing_time(60)
        self.set_charge(250)


class Class2Truck(Vehicle):
    def __init__(self):
        super().__init__("Class 2 Truck")
        self.set_servicing_time(120)
        self.set_charge(700)