import pandas as pd
from models.schedule import Schedule
from models.vehicle import get_vehicle_by_type

TODAY = "2022-10-04"

profit = 0
loss = 0

df = pd.read_csv(
    "resources/test.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)


def filter_by_appointment_date(date):
    return df.loc[df["appointment_date"].str.contains(date)]


def load_schedules(date):
    requests_by_date = filter_by_appointment_date(date)
    requests_by_date.sort_values(by="request_date")

    BAYS = {
        "compact": Schedule(date),
        "medium": Schedule(date),
        "full-size": Schedule(date),
        "class 1 truck": Schedule(date),
        "class 2 truck": Schedule(date),
    }

    def find_available_bay(date, vehicle):
        for bay in BAYS:
            if bay == "any" or bay == vehicle.type:
                if BAYS[bay].is_slot_available(date, vehicle):
                    print("added" + date)
                    return True
                else:
                    print("rejected" + date)
                    return False

    for _, request in requests_by_date.iterrows():
        vehicle = get_vehicle_by_type(request.vehicle_type)
        find_available_bay(request.appointment_date, vehicle)


load_schedules(TODAY)
