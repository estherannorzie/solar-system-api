from flask import Blueprint, jsonify

class Planets:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


# create our instances
planets = [
    Planets(1, "Mercury", "Small hot planet"),
    Planets(2, "Venus", "A gaseous planet"),
    Planets(3, "Earth", "Has lots of life")
]

# create the blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# do the decorator
@planets_bp.route("", methods=["GET"])
def get_all_planets():
    return jsonify([
        {"id": planet.id,
        "name": planet.name,
        "description": planet.description} 
        for planet in planets
    ])