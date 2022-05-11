from app import db

class Moon(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String)
  size = db.Column(db.Integer)
  description = db.Column(db.String)
  planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
  planets = db.relationship("Planet", back_populates="moon")

  @classmethod
  def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
                description=data_dict["description"],
                moons=data_dict["moons"],
                size=data_dict["size"],
                planet_id=data_dict["planet_id"]
                )

  def to_dict(self):
    return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "size": self.size,
                "planet_id": self.planet_id
            }