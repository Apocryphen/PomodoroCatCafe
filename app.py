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

from flask_bootstrap import Bootstrap

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)
data = [{
  "name": "bootstrap-table",
  "commits": "10",
  "attention": "122",
  "uneven": "An extended Bootstrap table"
},
 {
  "name": "multiple-select",
  "commits": "288",
  "attention": "20",
  "uneven": "A jQuery plugin"
}, {
  "name": "Testing",
  "commits": "340",
  "attention": "20",
  "uneven": "For test"
}]
# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
columns = [
  {
    "field": "name", # which is the field's name of data key
    "title": "name", # display as the table header's name
    "sortable": True,
  },
  {
    "field": "commits",
    "title": "commits",
    "sortable": True,
  },
  {
    "field": "attention",
    "title": "attention",
    "sortable": True,
  },
  {
    "field": "uneven",
    "title": "uneven",
    "sortable": True,
  }
]

#jdata=json.dumps(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)
