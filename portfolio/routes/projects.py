from flask import Blueprint, render_template
import yaml
import os

projects_view = Blueprint('projects', __name__, url_prefix='/projects' ,template_folder='\\templates', static_folder='\\static')

@projects_view.route('/')
def projects():
    yaml_file = os.path.join(os.path.dirname(__file__), '..\\info.yaml')
    with open(yaml_file) as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return render_template('projects_home.html',**data)