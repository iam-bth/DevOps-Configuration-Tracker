class ConfigItem:
    def __init__(self, name, version, environment, status):
        self.name = name
        self.version = version
        self.environment = environment
        self.status = status
            
    def to_dict(self):
        return {
            "name": self.name,
            "version": self.version,
            "environment": self.environment,
            "status": self.status
        }
        
    @staticmethod
    def from_dict(data):
        return ConfigItem(
            name = data["name"],
            version = data["version"],
            environment = data["environment"],
            status = data["status"]
        )