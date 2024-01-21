from . import app, cross_origin, request, jsonify
from services.schedule_service import get_schedule_by_date


@app.route("/schedule", methods=["POST"])
@cross_origin()
def get_schedule():
    date = request.json["date"]
    schedule = get_schedule_by_date(date)
    return jsonify(schedule.to_dict())
