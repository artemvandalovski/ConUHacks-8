from models.vehicle import Vehicle, VehicleType
from models.request import Request
from service.request_service import RequestValidator

# request = Request("2024-01-20 10:00:00", "2024-10-15 14:30:00", "Car")
# validator = RequestValidator(request)
# validator.validate_dates()

# if validator.valid:
#     print("Request is valid.")
# else:
#     print(f"Invalid request: {validator.error_message}")

print(VehicleType.CLASS_1_TRUCK.name)
