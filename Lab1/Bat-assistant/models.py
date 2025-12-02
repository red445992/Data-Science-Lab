class criminal:
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
        return criminal(
            name=data["name"],
            threat=data["threat"],
            last_seen=data["last_seen"]
        )
class Mission:
    def __init__(self,description,target_criminal,piority,status):
        self.description = description
        self.target_criminal = target_criminal
        self.piority = piority
        self.status = status
    def to_dict(self):
        return {
            "description": self.description,
            "target_criminal": self.target_criminal,
            "piority": self.piority,
            "status": self.status
        }
    @staticmethod
    def from_dict(data):
        return Mission(
            description=data["description"],
            target_criminal=data["target_criminal"],
            piority=data["piority"],
            status=data["status"]
        )