from flask import Blueprint, jsonify, abort, make_response, request
from app.models.moon import Moon
from app import db
from .planet_routes import jsonify_message, validate_planet, planets_bp

# moon_bp = Blueprint("moons", __name__, url_prefix="/moons")

# @moon_bp.route("<planet_id>/moons", methods=["POST"])
# def create_moon(planet_id):
#     planet = validate_planet(planet_id)
#     request_body = request.get_json()
#     # new_moon = Moon.from_dict(request_body)
#     new_moon = Moon(name = request_body['name'], 
#          size = request_body['size'],
#          description = request_body['description'],
#          planet_id = planet_id)

#     db.session.add(new_moon)
#     db.session.commit()

#     return jsonify_message(f"Moon {new_moon.name} successfully created", 201)