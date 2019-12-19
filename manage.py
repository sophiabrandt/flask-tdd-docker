from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    """Recreates the database."""
    db.session.remove()
    db.drop_all()
    db.create_all()


@cli.command("seed_db")
def seed_db():
    """Seeds the database."""
    db.session.add(User(username="angela", email="angela1@myemail.com"))
    db.session.add(User(username="cathy", email="cathy@notreal.com"))
    db.session.commit()


if __name__ == "__main__":
    cli()
