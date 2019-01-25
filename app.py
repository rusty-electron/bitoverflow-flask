from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user, LoginManager, login_required, login_user, logout_user
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound

import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoyohoneysingh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oauth/login.db'

github_bp = make_github_blueprint(client_id='4035f36da25790d28f88', client_secret='2132f2e71596a9b7d19d1550e683adec7bec8642')
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

github_bp.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user, user_required=False)

print(__name__=="__main__")

@app.route("/")
def home():
    return render_template("index.html", data=current_user)

@app.route("/guide")
def guide():
    return render_template("guide.html",  data=current_user)

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
            db.session.commit()

        login_user(user)


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", data=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
