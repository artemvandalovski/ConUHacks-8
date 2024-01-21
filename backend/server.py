from flask import Flask, jsonify, request
from services.schedule_service import generate_schedule_by_date

app = Flask(__name__)


@app.route("/schedule", methods=["POST"])
def generate_schedule():
    date = request.json["date"]
    schedule = generate_schedule_by_date(date)
    return jsonify(schedule.__dict__)


if __name__ == "__main__":
    app.run(debug=True)
