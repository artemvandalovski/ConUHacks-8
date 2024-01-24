from routes import app
from services import schedule_service
import threading


def main():
    schedule_thread = threading.Thread(target=schedule_service.create_all_schedules)
    schedule_thread.start()
    app.run(debug=True)


if __name__ == "__main__":
    main()
