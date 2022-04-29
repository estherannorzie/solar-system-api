from flask import Blueprint, jsonify, abort, make_response
from app.models.planet import Planet
from app import db

# class Planets:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description


# create our instances
# planets = [
#     Planets(1, "Mercury", "Small hot planet"),
#     Planets(2, "Venus", "A gaseous planet"),
#     Planets(3, "Earth", "Has lots of life")
# ]

# create the blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


# do the decorator
# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     return jsonify([
#          to_dict(planet)
#         for planet in planets
#   ])

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_one_planet(planet_id):

#     planet = validate_planet(planet_id)

#     return jsonify(to_dict(planet))

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         abort(make_response({"message": f"invalid id {planet_id}"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
#     abort(make_response({"message": f"planet id {planet_id} not found"}, 404))