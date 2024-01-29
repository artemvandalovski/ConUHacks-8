from . import app, cross_origin, jsonify
from ..services.schedule_service import get_schedule_by_date


@app.route("/schedule/<date>", methods=["GET"])
@cross_origin()
def get_schedule(date):
    schedule = get_schedule_by_date(date)
    if schedule:
        return jsonify(schedule.to_dict())
    return jsonify({"error": "Schedule not found"}), 404
