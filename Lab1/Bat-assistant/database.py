import os,json
from models import Mission, criminal


criminal_data_path = "data/criminals.json"
mission_data_path = "data/missions.json"
def load_criminals():
    if not os.path.exists(criminal_data_path):
        return []

    with open(criminal_data_path, "r") as file:
        data = json.load(file)
        return [criminal.from_dict(c) for c in data]


def save_criminals(criminals):
    with open(criminal_data_path, "w") as file:
        json.dump([c.to_dict() for c in criminals], file, indent=4)


def load_missions():
    if not os.path.exists(mission_data_path):
        return []

    with open(mission_data_path, "r") as file:
        data = json.load(file)
        return [Mission.from_dict(m) for m in data]


def save_missions(missions):
    with open(mission_data_path, "w") as file:
        json.dump([m.to_dict() for m in missions], file, indent=4)