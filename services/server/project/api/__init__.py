from flask_restx import Api

from project.api.address.views import address_namespace
from project.api.persons.views import person_namespace

api = Api(version="1.0", title="Flask SqlAlchemy Relationship Test", doc="/docs")

api.add_namespace(address_namespace, path="/address")
api.add_namespace(person_namespace, path="/person")
