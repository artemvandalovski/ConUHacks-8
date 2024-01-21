from services.schedule_service import get_schedule_by_date

schedule = get_schedule_by_date("2022-10-05")
print(schedule.date)
