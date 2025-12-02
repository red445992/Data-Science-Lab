class Criminal:
    def __init__(self, name, threat, last_seen):
        self.name = name
        self.threat = threat
        self.last_seen = last_seen

    def to_dict(self):
        return {
            "name": self.name,
            "threat": self.threat,
            "last_seen": self.last_seen
        }

    @staticmethod
    def from_dict(data):
        return Criminal(
            name=data["name"],
            threat=data["threat"],
            last_seen=data["last_seen"]
        )
