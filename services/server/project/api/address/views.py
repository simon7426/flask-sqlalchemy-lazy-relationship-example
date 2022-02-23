from flask import current_app, request
from flask_restx import Namespace, Resource, fields

from project.api.address.cruds import add_address, get_all_addresses

address_namespace = Namespace("address")

address_model = address_namespace.model(
    "Address",
    {
        "id": fields.Integer(readOnly=True),
        "address": fields.String(required=True),
        "person_id": fields.Integer(required=True),
        "created_at": fields.DateTime(readOnly=True),
    },
)


@address_namespace.route("", endpoint="addresslist")
class Address(Resource):
    @address_namespace.marshal_with(address_model, as_list=True)
    def get(self):
        addresses = get_all_addresses()
        return addresses, 200

    @address_namespace.marshal_with(address_model)
    def post(self):
        try:
            post_data = request.get_json()
            address = post_data.get("address")
            person_id = post_data.get("person_id")

            address = add_address(address, person_id)
            return address, 201
        except Exception as e:
            current_app.logger.info(e)
            print(e)
            address_namespace.abort(400, "Operation error")
