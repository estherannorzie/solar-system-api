from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app.models.moon import Moon
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return jsonify_message(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    # new_moon = Moon.from_dict(request_body)
    new_moon = Moon(name = request_body['name'], 
         size = request_body['size'],
         description = request_body['description'],
         planet_id = planet_id)

    db.session.add(new_moon)
    db.session.commit()

    return jsonify_message(f"Moon {new_moon.name} successfully created", 201)


@planets_bp.route("/<planet_id>/moons", methods=["GET"])
def read_all_moons(planet_id):
    planet = validate_planet(planet_id)
    response = [moon.to_dict() for moon in planet.moon]

    return jsonify_message(response, 200)


@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else: 
        planets = Planet.query.all() 

    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return jsonify(planet.to_dict())


@planets_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet(planet_id):
    request_body = request.get_json()
    planet = validate_planet(planet_id)

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()
    
    return jsonify_message(f"Planet succesfully updated. {planet.to_dict()}")


@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()
    
    return jsonify_message("Planet succesfully deleted.", 200)
    
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
    return make_response(jsonify(message),status_code)