from flask import Blueprint, jsonify, abort, make_response, request
from app.models.planet import Planet
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    
    name_query = request.args.get("name")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    else: 
        planets = Planet.query.all() 
    # description_query = request.args.get("description")
    # if description_query:
    #     planets.extend(Planet.query.filter_by(description=description_query))
    
    # if not planets:
    #     planets = Planet.query.all()  

    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
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
    
    return make_response(jsonify(f"Planet succesfully updated. {planet.to_dict()}"))


@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()
    
    return make_response(jsonify(f"Planet succesffuly deleted."))

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"invalid id {planet_id}"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message": f"planet id {planet_id} not found"}, 404))
    return planet