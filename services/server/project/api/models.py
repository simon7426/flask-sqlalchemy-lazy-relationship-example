from datetime import datetime

from project import db


class Person(db.Model):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    address = db.relationship("Address", backref="person", lazy=True)

    def __init__(self, name: str) -> None:
        self.name = name


class Address(db.Model):
    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(128), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("persons.id"), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, address: str, person_id: int) -> None:
        self.address = address
        self.person_id = person_id
