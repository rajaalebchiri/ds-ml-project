from flask import Flask, render_template, request, url_for, redirect, session
from markupsafe import escape

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def hello_world():
    return render_template("index.html", session=session)

@app.route("/projects/<title>")
def show_project_details(title):
    return f"Project: {escape(title)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath: {escape(subpath)}"


@app.route("/profile")
def profile():
    username = session["username"]
    return render_template("profile.html", username=username)


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            session['username'] = request.form['username']
            return redirect(url_for("profile"))
        else:
            error = "Invalid Username/Password"
    return render_template('login.html', error=error)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("hello_world"))
