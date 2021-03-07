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
from app import create_app

app_instance = create_app()
if __name__ == '__main__':
    app_instance.run(debug=True)