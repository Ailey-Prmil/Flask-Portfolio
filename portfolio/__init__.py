from flask import Flask, render_template, request, url_for
import os

def page_not_found(e):
    return render_template("error.html", error_code=400, error_description="Page Not Found"), 400

def redirect_url(default='intro.home'):
    return request.referrer or url_for(default)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py", silent=True)
    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    with app.app_context():
        from .routes import intro
        app.register_blueprint(intro.intro_view)

        from .routes import skills
        app.register_blueprint(skills.skills_view)
        
        from .routes import admin, auth
        app.register_blueprint(auth.auth_view)
        app.register_blueprint(admin.admin_view)

        from .routes import projects
        app.register_blueprint(projects.projects_view)

        from .routes import contact
        app.register_blueprint(contact.contact_view)

        app.register_error_handler(400, page_not_found)
        app.add_template_global(redirect_url)
     
        return app
