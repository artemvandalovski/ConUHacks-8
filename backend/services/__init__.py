import pandas as pd

df = pd.read_csv(
    "resources/datafile.csv",
    header=None,
    names=["request_date", "appointment_date", "vehicle_type"],
)
