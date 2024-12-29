from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS
import json

# pip install flask-cors
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/newmessage", methods=["POST", "GET"])
def newMessage():
    if request.method == "POST":
        received_message = request.form
        saveNewMessage(received_message)
        return "<p>Vastaanotettu.</p>"
    else:
        return "<p>Ei vastaanotettu.</p>"

# Tallennetaan vastaanotettu viesti JSON muodossa.
def saveNewMessage(message):
    newMessage = json.dumps({"message": str(message)})
    

@app.route("/findmessage", methods=["GET"])
def findMessage():
    return json.dumps({"message": "Kokeiluviesti on nyt tässä!.,?"})
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)