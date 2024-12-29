from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS
import json

# pip install flask-cors
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Vastaanotetaan uusi viesti tallennettavaksi.
@app.route("/newmessage", methods=["POST", "GET"])
def newMessage():
    if request.method == "POST":
        received_message = request.data
        saveMessage(str(received_message))
        return "<p>Vastaanotettu.</p>"
    else:
        return "<p>Ei vastaanotettu.</p>"

# Tallennetaan vastaanotettu viesti JSON muodossa.
def saveMessage(message):
    newJson = {"message": message}
    with open("messages.json", "r+") as f:
        load_data = json.load(f)
        load_data["allMessages"].append(newJson)
        f.seek(0)
        json.dump(load_data, f, indent=4)

# Palautetaan kaikki tallennetut viestit.
@app.route("/findmessage", methods=["GET"])
def findMessage():
    f = open("messages.json")
    data = json.load(f)
    f.close()
    return data

    
@app.route("/removemessage", methods=["POST"])
def removemessage():
    cleanMessages = {"allMessages": []}
    with open("messages.json", "w") as f:
        json.dump(cleanMessages, f)
    return "Jee"



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', person=name)

#{
#    "allMessages": [
#           
#    ]
#}

#{"allMessages": [{"message": "Koiro"}]}