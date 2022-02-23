from sqlalchemy.orm import joinedload

from project import db
from project.api.models import Person


def get_all_persons():
    return Person.query.all()


def add_person(name):
    person = Person(name=name)
    db.session.add(person)
    db.session.commit()
    return person


def get_person_by_id(id):
    return Person.query.filter_by(id=id).first()


def get_person_address_multiple_query(id):
    person = Person.query.filter_by(id=id).first()
    address = person.address
    return address


def get_person_address_single_query(id):
    person = Person.query.filter_by(id=id).options(joinedload("address")).first()
    address = person.address
    return address
