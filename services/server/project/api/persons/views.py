from flask import request
from flask_restx import Namespace, Resource, fields

from project.api.persons.cruds import (
    add_person,
    get_all_persons,
    get_person_address_multiple_query,
    get_person_address_single_query,
)

person_namespace = Namespace("person")

person_model = person_namespace.model(
    "Person",
    {
        "id": fields.Integer(readOnly=True),
        "name": fields.String(required=True),
        "created_at": fields.DateTime(readOnly=True),
    },
)


address_model = person_namespace.model(
    "Address",
    {
        "id": fields.Integer(readOnly=True),
        "address": fields.String(required=True),
        "person_id": fields.Integer(required=True),
        "created_at": fields.DateTime(readOnly=True),
    },
)


@person_namespace.route("", endpoint="personlist")
class Person(Resource):
    @person_namespace.marshal_with(person_model, as_list=True)
    def get(self):
        persons = get_all_persons()
        return persons, 200

    @person_namespace.marshal_with(person_model)
    def post(self):
        post_data = request.get_json()
        name = post_data.get("name")

        person = add_person(name)
        return person, 201


@person_namespace.route("/<int:id>/address", endpoint="person-address")
class PersonAddress(Resource):
    @person_namespace.marshal_with(address_model, as_list=True)
    def get(self, id):
        address = get_person_address_multiple_query(id)
        return address, 200


@person_namespace.route("/<int:id>/address/single", endpoint="person-address-single")
class PersonAddressSingle(Resource):
    @person_namespace.marshal_with(address_model, as_list=True)
    def get(self, id):
        address = get_person_address_single_query(id)
        return address, 200
