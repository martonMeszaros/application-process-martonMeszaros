from flask import Flask, redirect, url_for

import display
app = Flask(__name__)


@app.route("/")
def index():
    return display.index()


@app.route("/mentors")
def mentors():
    return display.mentors()


@app.route("/all-school")
def all_school():
    return display.all_school()


@app.route("/mentors-by-country")
def mentors_by_country():
    return display.mentors_by_country()


@app.route("/contacts")
def contacts():
    return display.contacts()


@app.route("/applicants")
def applicants():
    return display.applicants()


@app.route("/applicants-and-mentors")
def applicants_and_mentors():
    return display.applicants_and_mentors()


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
