from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)
    moon = db.relationship("Moon", back_populates="planets")

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "moons": self.moons
            }
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
                description=data_dict["description"],
                moons=data_dict["moons"]
                )