from flask import Blueprint, render_template, abort
import yaml
import os
from urllib.parse import unquote

def skill_tag_included(skill, data):
    result = []
    for skill_info in data:
        try:
            if skill in skill_info["skills_included"]:
                result.append(skill_info)
        except:
            pass
    return result


skills_view = Blueprint("skills",__name__, url_prefix="/skills", template_folder="\\templates", static_folder="\\static",)

@skills_view.route('/')
def skills():
    yaml_file = os.path.join(os.path.dirname(__file__), "..\\info.yaml")
    with open (yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        skill_tags = data["skill_tags"]
        data = data["skills"]
        data = {"skills": data, "skill_tags": skill_tags}
    return render_template("skills.html", **data)
@skills_view.route('/<skill>')
def skill_details(skill):
    skill = unquote(skill)
    yaml_file = os.path.join(os.path.dirname(__file__), "..\\info.yaml")
    with open (yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        skill_data = data["skills"]["Soft_Skills"]+data["skills"]["Hard_Skills"]
        validCheck = False
        for skill_info in skill_data:
            if skill_info["name"] == skill:
                skill_data = skill_info
                validCheck = True
                break
        if not validCheck:
            abort(400)
        extra = {}
        for section, status in data["config"].items():
            if status and section not in ["about_me", "educations"]:
                extra_info = skill_tag_included(skill, data[section])
                if (extra_info):
                    extra[section] = extra_info
    
    data = {"skill": skill, 
            "skill_data": skill_data, 
            "extra": extra}
    
    print (data)
    return render_template("skill_details.html", **data)