from . import db_path, SqliteDict, dumps, loads


def get_schedule(date):
    with SqliteDict(db_path) as db:
        if date in db:
            return loads(db[date])
        return None


def save_schedule(schedule):
    with SqliteDict(db_path) as db:
        db[schedule.date] = dumps(schedule)
        db.commit()
