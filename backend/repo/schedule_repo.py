from . import SqliteDict, db_path
from models.schedule import Schedule


def get_schedule(date):
    with SqliteDict(db_path) as db:
        print(f"Getting schedule for {date}")
        schedule = db.get(date)
        if schedule:
            print(f"Got schedule for {date}")
            return Schedule.from_dict(schedule)
        print(f"Schedule for {date} not found")
        return None


def save_schedule(schedule):
    with SqliteDict(db_path) as db:
        print(f"Saving schedule for {schedule.date}")
        db[schedule.date] = schedule.to_dict()
        db.commit()
        print(f"Saved schedule for {schedule.date}")
        return schedule
