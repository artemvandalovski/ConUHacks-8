import threading

from app.routes import app
from app.services import schedule_service


def main():
    schedule_thread = threading.Thread(target=schedule_service.create_all_schedules)
    schedule_thread.start()
    app.run(debug=True)


if __name__ == "__main__":
    main()
