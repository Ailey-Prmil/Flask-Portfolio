from flask import Blueprint, render_template, request, session, redirect, url_for, current_app, g, flash
from werkzeug.security import check_password_hash
from functools import wraps

auth_view = Blueprint("auth",__name__, url_prefix="/auth", template_folder="\\templates", static_folder="\\static")
def login_required(view_func):
    @wraps(view_func)
    def check(*args, **kwargs):
        if  g.username == None:
            return redirect(url_for("auth.login"))

        return view_func(*args, **kwargs)
    return check
@auth_view.before_app_request
def load_user_logged_in():
    g.username = None
    if "username" in session:
        g.username = session["username"]

@auth_view.route('/login', methods=["GET", "POST"], endpoint="login")
def login():
    error = None
    if (request.method == "POST"):
        session["username"] = request.form["username"]
        if (request.form["username"] == "admin" and check_password_hash(current_app.config["PASSWORD_HASH"], request.form["password"])):
            if request.form.get("rememberMe")=="checked":
                session.permanent = True
            else:
                session.permanent = False
            return redirect(url_for("admin.admin"))
        else:
            error = "Invalid credentials"
    flash(error)
    return render_template("auth.html", error=error)