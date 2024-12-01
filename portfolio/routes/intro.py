from flask import Blueprint, render_template
import os
import yaml

intro_view = Blueprint("intro",__name__, url_prefix="/", template_folder="\\templates", static_folder="\\static",)

@intro_view.route("/")
def home():
    yaml_file = os.path.join(os.path.dirname(__file__), "..\\info.yaml")
    with open (yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return render_template("intro.html", **data)