from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


"""Model for Pet Adoption Agency."""


class Pet(db.Model):
    """Creates Pet model"""

    __tablename__ = "pets"

    def __repr__(self):
        """Show info about pets"""
        u = self
        return f"<Pet id={u.id} name={u.name} species={u.species}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    @classmethod
    def get_all_pets(cls):
        return cls.query.all()
