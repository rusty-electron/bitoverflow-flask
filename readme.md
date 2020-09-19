## BitOverflow - Flask

This repository contains the site code for the website [bitoverflow.in](https://bitoverflow.in) that was created to host the event BitOverflow organized under Techxom '19. Visit its [organization Page](https://github.com/bitoverflow-in/)

This website primarily uses the following tools:
* Flask
* Flask-SQLAlchemy
* Flask-login
* SQLite3
* PyGithub

### Instructions to Deploy locally

*Detailed Installation Steps will be added soon, Hang tight!*

Note: To deploy as Production Server, don't use this method rather create a WSGI file and deploy using it.

1. Create a virtual environment (Optional)
1. Install dependencies from `requirements.txt` using the command:
```markdown
pip install -r requirements.txt
```
1. Run `app.py`
1. To update leaderboard, run `database.py`. (It is advise to create a scheduled task for it.) 
