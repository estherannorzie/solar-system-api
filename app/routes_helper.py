from flask import jsonify, abort, make_response
from app.models.planet import Planet


def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"invalid id {planet_id}"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet id {planet_id} not found"}, 404))
    return planet


def jsonify_message(message, status_code):
    return make_response(jsonify(message), status_code)