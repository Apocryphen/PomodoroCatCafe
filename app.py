# Welcome to the Pomodoro cat cafe Flask-Bootstrap application . This will give you a
# guided tour around creating an application using Flask-Bootstrap.
#
# To run this application yourself, please install its requirements first:
#
#   $ pip install -r sample_app/requirements.txt
#
# Then, you can actually run the application.
#
#   $ flask --app=sample_app dev
#
# Afterwards, point your browser to http://localhost:5000, then check out the
# source.

from flask import Flask, render_template

from flask_bootstrap import Bootstrap

def create_app(configfile=None):
    # We are using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/
    from flask import Flask, render_template
    from flask_bootstrap import Bootstrap
    app = Flask(__name__)
    # Install our Bootstrap extension
    Bootstrap(app)
    import frontend

    return app