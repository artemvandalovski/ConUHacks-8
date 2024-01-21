from flask import Flask, jsonify, request
from services.schedule_service import get_schedule_by_date

app = Flask(__name__)


@app.route("/schedule", methods=["POST"])
def get_schedule():
    date = request.json["date"]
    schedule = get_schedule_by_date(date)
    return jsonify(schedule.to_dict())


if __name__ == "__main__":
    app.run(debug=True)
