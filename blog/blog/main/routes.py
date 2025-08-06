from flask import Blueprint
from flask import render_template, request, Blueprint
from blog.models import Post, User

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page= page, per_page = 3)
    return render_template("home.html.j2", posts = posts)

@main.route("/about")
def about():
    return render_template("about.html.j2", title = "About")

@main.route("/announcements")
def announcements():
    page = request.args.get("page", 1, type = int)
    users = User.query.paginate(page= page, per_page = 3)
    posts = {}
    for user in users:
        posts[user] = Post.query.filter_by(author= user).count()
    return render_template("announcements.html.j2", title = "Announcements", users= users, posts= posts)