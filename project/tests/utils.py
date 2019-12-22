from project import db
from project.api.users.models import User


def recreate_db():
    db.session.remove()
    db.drop_all()
    db.create_all()


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user
