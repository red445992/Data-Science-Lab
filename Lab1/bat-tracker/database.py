import json
import os
from models import Criminal

DATA_PATH = "data/criminals.json"

def load_criminals():
    if not os.path.exists(DATA_PATH):
        return []

    with open(DATA_PATH, "r") as file:
        data = json.load(file)
        return [Criminal.from_dict(c) for c in data]


def save_criminals(criminals):
    with open(DATA_PATH, "w") as file:
        json.dump([c.to_dict() for c in criminals], file, indent=4)
