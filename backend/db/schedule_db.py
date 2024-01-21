import sqlitedict
from models.schedule import Schedule

db_path = "schedule_db.sqlite"


def get_schedule(date):
    with sqlitedict.SqliteDict(db_path) as db:
        return Schedule.from_dict(db[date])


def save_schedule(schedule):
    with sqlitedict.SqliteDict(db_path) as db:
        db[schedule.date] = schedule.to_dict()
