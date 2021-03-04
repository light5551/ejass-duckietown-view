import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "supersekrit")
app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")
github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")



@app.route("/")
def index():
    return "<h1>check</h1>"


if __name__ == '__main__': app.run(debug=True)

    #'''
    #if not github.authorized:
    #    return redirect(url_for("github.login"))
    #resp = github.get("/user")
    #if resp.ok:
    #    return "You are @{login} on GitHub".format(login=resp.json()["login"])
    #return "<h1>Ooops!</h1>"
    #'''
    