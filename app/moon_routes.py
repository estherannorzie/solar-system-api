from flask import Blueprint, jsonify, abort, make_response, request
from app.models.moon import Moon
from app import db
from .routes_helper import validate_planet, jsonify_message

moons_bp = Blueprint("moons", __name__, url_prefix="/moons")

@moons_bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    new_moon = Moon(name = request_body['name'], 
                    size = request_body['size'],
                    description = request_body['description'],
                    planet = planet)

    db.session.add(new_moon)
    db.session.commit()

    return jsonify_message(f"Moon {new_moon.name} successfully created", 201)


@moons_bp.route("/<planet_id>/moons", methods=["GET"])
def read_all_moons(planet_id):
    planet = validate_planet(planet_id)
    response = [moon.to_dict() for moon in planet.moon]
    return jsonify_message(response, 200)