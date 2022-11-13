# Contains the backend server
__author__ = "Matteo Golin"

# Imports
from utils import load_plants_from_csv, load_environments_from_csv
from classes.forest import Forest
from flask import Flask, request
from flask_cors import CORS, cross_origin

# Constants
def print_row(row):
    print([_.name[0] if _ else " " for _ in row])

# Main
app = Flask(__name__)  # Create server
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


# Starting data
plant_dicts = load_plants_from_csv()
environments = load_environments_from_csv()
forest = Forest(
    width=100,
    height=100,
    environment=environments["pukaskwa"],
    plants=plant_dicts
)


# Endpoints
@app.route("/increment", methods=["POST"])
@cross_origin()
def increment():
    global forest
    forest.increment(request.json["month"])
    return forest.json()


@app.route("/start", methods=["POST"])
@cross_origin()
def start():
    environment = request.json.get("environment")
    global forest
    forest = Forest(
        width=100,
        height=100,
        environment=environments[environment],
        plants=plant_dicts
    )
    forest.populate()
    return {'status': 200}


if __name__ == '__main__':
    app.run(port=8000, debug=True)
