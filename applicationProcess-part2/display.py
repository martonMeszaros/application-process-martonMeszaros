from flask import render_template

import data_manager


def index():
    return render_template("index.html")


def mentors():
    return render_template("mentors.html", query=data_manager.mentors())


def all_school():
    return render_template("all_school.html", query=data_manager.all_school())


def mentors_by_country():
    return render_template("mentors_by_country.html", query=data_manager.mentors_by_country())


def contacts():
    return render_template("contacts.html", query=data_manager.contacts())


def applicants():
    return render_template("applicants.html", query=data_manager.applicants())


def applicants_and_mentors():
    return render_template("applicants_and_mentors.html", query=data_manager.applicants_and_mentors())
