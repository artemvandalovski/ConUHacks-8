import pandas as pd
from models.request import Request
from models.vehicle import VEHICLES

# validate request
# is slot available
# 5 free bays and 1 bay for each vehicle type


df = pd.read_csv(
    "resources/datafile.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)
df.sort_values(by=["request_date"], inplace=True)


def get_requests_by_date(date):
    return df.loc[df["request_date"] == date]


def load_schedule():
    for request in df.iterrows():
        pass


def get_available_bays():
    pass


def is_slot_available(request):
    pass


def get_vehicle(vehicle_type):
    for vehicle in VEHICLES:
        if vehicle.vehicle_type == vehicle_type:
            return vehicle
