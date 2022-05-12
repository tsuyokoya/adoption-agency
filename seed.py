"""Seed file to make sample data for adoption db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Sample pets
pets = [
    Pet(
        name="Mr. What",
        species="cat",
        photo_url="https://images.unsplash.com/photo-1555685812-4b943f1cb0eb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8cGV0c3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60",
        age=5,
        notes="Yes, he always looks confused",
    ),
    Pet(
        name="Butters",
        species="hamster",
        photo_url="https://images.unsplash.com/photo-1425082661705-1834bfd09dca?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=876&q=80",
        age=30,
        notes="Immortal hamster. Feeds off of human souls.",
    ),
    Pet(
        name="Al Pacino",
        species="alpaca",
        photo_url="https://images.unsplash.com/photo-1552474705-dd8183e00901?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NzN8fGFuaW1hbHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60",
        age=3,
        notes="Say hello to my little friend!",
    ),
    Pet(
        name="Hot Dog",
        species="dog",
        photo_url="https://images.unsplash.com/photo-1618265341355-d0e2d1fdf26b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80",
        age=13,
        notes="Hot Dog mastered levitation.",
    ),
    Pet(
        name="Happy",
        species="cat",
        photo_url="https://images.unsplash.com/photo-1588768987479-bcebeefb8a5c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
        age=6,
        notes="He is happy. Just take my word for it.",
    ),
    Pet(
        name="Fluff",
        species="alpaca",
        photo_url="https://images.unsplash.com/photo-1589182337358-2cb63099350c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
        age=8,
        notes="A great ball of floof.",
    ),
]

# Add new objects to session
db.session.bulk_save_objects(pets)
db.session.commit()
