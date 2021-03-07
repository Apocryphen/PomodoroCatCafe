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

from flask import Flask, render_template, request
import threading
import atexit

from flask_bootstrap import Bootstrap

"""
A example for creating a Table that is sortable by its header
"""
POOL_TIME = 5 #Seconds

# variables that are accessible from anywhere
commonDataStruct = {}
# lock to control access to variable
dataLock = threading.Lock()
# thread handler
yourThread = threading.Thread()

def create_app():
    app = Flask(__name__)

    def interrupt():
        global yourThread
        yourThread.cancel()

    def doStuff():
        global commonDataStruct
        global yourThread
        with dataLock:
        # Do your stuff with commonDataStruct Here
            print("test")
        # Set the next thread to happen
            yourThread = threading.Timer(POOL_TIME, doStuff, ())
            yourThread.start()

    def doStuffStart():
        # Do initialisation stuff here
        global yourThread
        # Create your thread
        yourThread = threading.Timer(POOL_TIME, doStuff, ())
        yourThread.start()

    # Initiate
    doStuffStart()
    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)
    return app

app = create_app()
time = 0
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", time)


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)
