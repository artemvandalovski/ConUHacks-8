from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

app.config["CORS_HEADERS"] = "Content-Type"

from app.routes import schedule_routes
