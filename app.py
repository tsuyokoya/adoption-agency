"""Adoption Agency application."""

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
from models import db, connect_db, Pet
import os

app = Flask(__name__)

# Specify the database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"

# Default is True, turn off to prevent overhead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Prints all SQL statements to terminal
app.config["SQLALCHEMY_ECHO"] = True

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "something"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def show_home_page():
    """Show homepage list of pets"""

    all_pets = Pet.get_all_pets()
    return render_template("home.html", all_pets=all_pets)


@app.route("/add", methods=["GET", "POST"])
def show_add_pet_form():
    """Show form to add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        # set default image if no image provided
        photo_url = form.photo_url.data
        if not photo_url:
            photo_url = "https://thumbs.dreamstime.com/b/cartoon-dog-as-logo-symbol-pet-care-vector-illustration-212070807.jpg"
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name}!")
        return redirect("/")
    else:
        return render_template("addpetform.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Show pet details and edit form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        if not pet.photo_url:
            pet.photo_url = "https://thumbs.dreamstime.com/b/cartoon-dog-as-logo-symbol-pet-care-vector-illustration-212070807.jpg"
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        flash(f"Updated {pet.name}!")
        return redirect(f"/{pet_id}")
    else:
        return render_template("petdetails.html", form=form, pet=pet)
