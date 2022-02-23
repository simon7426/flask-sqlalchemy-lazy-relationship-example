from project import db
from project.api.models import Address


def get_all_addresses():
    return Address.query.all()


def add_address(address, person_id):
    address = Address(
        address=address,
        person_id=person_id,
    )
    db.session.add(address)
    db.session.commit()
    return address
