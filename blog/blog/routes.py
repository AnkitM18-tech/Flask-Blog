import json
from blog import app
from flask import render_template, url_for, flash, redirect
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post


with open("posts.json") as f:
    posts = json.load(f)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html.j2", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html.j2", title = "About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html.j2", title = "Register", form = form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Logged in as {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("login.html.j2", title = "Sign In", form = form)