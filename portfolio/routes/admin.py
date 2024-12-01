from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from . import auth
from portfolio.lib.get_yaml_data import get_yaml_data

#from portfolio.controllers import user_controller
admin_view = Blueprint("admin",__name__, url_prefix="/admin", template_folder="\\templates", static_folder="\\static")

@admin_view.route('/', methods=["GET", "POST"])
@auth.login_required
def admin():
    data = get_yaml_data()
    if request.method == "POST":
        for key, value in request.form.items():
            print (key, value)

    return render_template("admin.html", **data)