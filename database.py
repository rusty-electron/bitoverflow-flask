from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oauth/login.db'
db = SQLAlchemy(app)

from project import projectList

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

    def __init__(self, username):
        self.username = username

#list of all usernames
users = userInfo.query.all()
users_list=[]
for user in users:
    user.pr_count=0
    user.commit_count=0
    user.line_add=0
    user.line_delete=0
    user.pr_open=0
    
    users_list.append(user.username)

# PyGithub stuff
from github import Github

g = Github("<insert>")
repo_list = [ item.url[19:] for item in projectList ]
# for item in repo_list:
#     print(item)

for repo in repo_list:
    repo_main = g.get_repo(repo)
    pulls = repo_main.get_pulls(state='all', sort='created', base='master')

    for pr in pulls:
        if pr.user.login in users_list:
            found_user = userInfo.query.filter_by(username=pr.user.login).first()
            found_user.name = pr.user.name
            found_user.user_link = pr.user.html_url
            if pr.merged==True:
                found_user.pr_count+=1
                found_user.commit_count+=pr.commits
                found_user.line_add+=pr.additions
                found_user.line_delete+=pr.deletions
            if pr.state=="open":
                found_user.pr_open+=1

db.session.commit()