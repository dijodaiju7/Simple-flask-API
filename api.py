import flask
from flask import request, jsonify

#Defining name of the application
app = flask.Flask(__name__)
#To enable debug and state output in terminal
app.config["DEBUG"] = True

#Creating student data as dictionary
students = [
    {
    'id': 'S001',
     'name': 'Sidharth',
     'class': 'ME',
     'department': 'Mechanical'
     },

    {
    'id': 'S002',
     'name': 'Jake',
     'class': 'CSE',
     'department': 'Computer Science',},

    {'id': 'S003',
     'name': 'Vinod',
     'class': 'CE',
     'department': 'Civil'}
]




# A route to return student dictionary.
@app.route('/api/students', methods=['GET'])
def api_all():
    #Converting dictionary to json representation
    return jsonify(students)

app.run()