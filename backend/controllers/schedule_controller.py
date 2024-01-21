from . import app, request, jsonify
from services.schedule_service import get_schedule_by_date


@app.route("/schedule", methods=["POST"])
def get_schedule():
    date = request.json["date"]
    schedule = get_schedule_by_date(date)
    return jsonify(schedule.to_dict())
