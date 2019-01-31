from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import desc

from project import projectList

import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoyohoneysingh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oauth/login.db'

github_bp = make_github_blueprint(client_id='99e1b3c00d561e8b5d8c', client_secret='c6bfe7353ef012d67d3823ff218f7b4961165779')
app.register_blueprint(github_bp, url_prefix="/github_login")

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    name = db.Column(db.String)
    profile_link = db.Column(db.String)
    email = db.Column(db.String)
    avatar = db.Column(db.String)

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

class userInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    name = db.Column(db.String)
    user_link = db.Column(db.String)

    pr_count = db.Column(db.Integer, default=0)
    commit_count = db.Column(db.Integer, default=0)
    pr_open = db.Column(db.Integer, default=0)
    line_add = db.Column(db.Integer, default=0)
    line_delete = db.Column(db.Integer, default=0)

    def __init__(self, username, name, user_link):
        self.username = username
        self.name = name
        self.user_link = user_link

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

github_bp.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user, user_required=False)

print(__name__=="__main__")

message = ['choose your projects', 'main-stream projects']

@app.route("/")
def home():
    return render_template("index.html", data=current_user, msg = message)

# stats routes 
@app.route("/stats")
def stats():
    all_info = userInfo.query.all()
    return render_template("stats.html", data=current_user, info=all_info)

@app.route("/stats/<int:id>", methods = ["GET"])
def stats_order(id):
    if id==1:
        all_info = userInfo.query.order_by(userInfo.name).all()
    elif id==2:
        all_info = userInfo.query.order_by(userInfo.username).all()
    elif id==3:
        all_info = userInfo.query.order_by(desc(userInfo.pr_count)).all()
    else:
        all_info = userInfo.query.order_by(desc(userInfo.commit_count)).all()

    return render_template("stats.html", data=current_user, info=all_info)

# stats routes end
@app.route("/guide")
def guide():
    return render_template("guide.html",  data=current_user)

@app.route("/about")
def about():
    return render_template("about.html",  data=current_user)

@app.route("/projects")
def projects():
    return render_template("projects.html",  data=current_user, list=projectList)

@app.route("/github")
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    account_info = github.get("/user")

    account_info_json = account_info.json()
    print(account_info_json)
    username = account_info_json['login']
    return redirect(url_for('profile'))

@oauth_authorized.connect_via(github_bp)
def github_logged_in(blueprint, token):
    account_info = blueprint.session.get("/user")

    if account_info.ok:
        account_info_json = account_info.json()
        username = account_info_json['login']
        name = account_info_json['name']
        profile_link = account_info_json['html_url']
        email = account_info_json['email']
        avatar = account_info_json['avatar_url']

        query = User.query.filter_by(username = username)

        try: 
            user = query.one()
        except NoResultFound:
            user = User(username = username, name=name, profile_link=profile_link, email=email, avatar=avatar)
            db.session.add(user)

            userdata = userInfo(username = username, name=name, user_link=profile_link)
            db.session.add(userdata)
            db.session.commit()

        login_user(user)


@app.route("/profile")
@login_required
def profile():
    found_info = userInfo.query.filter_by(username = current_user.username).first()
    return render_template("profile.html", data=current_user, info=found_info, msg = message)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
