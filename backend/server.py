from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS
# pip install flask-cors
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/newmessage", methods=["POST", "GET"])
def newmessage():
    if request.method == "POST":
        received_message = request.form
        if len(received_message) > 10:
            return str(len(received_message)) + str(received_message)
        else: 
            return "Viesti on liian lyhyt."

@app.route("/getmessages", methods=["POST", "GET"])
def getmessages():
    if request.method =="GET":
        return "Yippii"
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)