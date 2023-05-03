"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
jackson_family = FamilyStructure("Jackson")
jackson_family.add_member({
    "id": jackson_family._generateId(),
    "first_name": "John" ,
    "age": 33,
    "Lucky Numbers": [7, 13, 22]
}),
jackson_family.add_member({
    "id": jackson_family._generateId(),
    "first_name": "Jane" ,
    "age": 35,
    "Lucky Numbers": [10, 14, 3]
}),
jackson_family.add_member({
    "id": jackson_family._generateId(),
    "first_name": "Jimmy" ,
    "age": 5,
    "Lucky Numbers": [1]
})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/member', methods=['POST'])
def handle_new_member():

    member = jackson_family.get_member(member_id)
    if member is None:
        raise APIException("Member not found", status_code=404)
        member = {
        "id": jackson_family._generateId(),
        "first_name": request_body.get("first_name", ""),
        "last_name": "Jackson",
        "age": request_body.get("age", 0),
        "lucky_numbers": request_body.get("lucky_numbers", [])
    }
    jackson_family.add_member(member)

    response_body = {
        "id": member["id"],
        "first_name": member["first_name"],
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"]
    }

    return jsonify(response_body), 200

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }
    
    return jsonify(response_body), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def handle_member(member_id):

    member = jackson_family.get_member(member_id)
    if member is None:
        raise APIException("Member not found", status_code=404)

    response_body = {
        "id": member["id"],
        "first_name": member["first_name"],
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"]
    }

    return jsonify(response_body), 200



@app.route('/member/<int:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):
    jackson_family.delete_member(member_id)
    if not deleted:
        raise APIException("Member not found", status_code=404)
    return jsonify({"msg": "Member deleted successfully"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
