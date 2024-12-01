from flask import Blueprint, render_template
from portfolio.lib.get_yaml_data import get_yaml_data


contact_view = Blueprint("contact",__name__, url_prefix="/contact", template_folder="\\templates", static_folder="\\static",)
@contact_view.route('/')
def contact():
    data = get_yaml_data()
    data = data["contact"]
    return render_template("contact.html", **data)