from flask import Flask, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Vastaanotetaan uusi viesti tallennettavaksi.
@app.route("/newmessage", methods=["POST", "GET"])
def newMessage():
    if request.method == "POST":
        #received_message = request.form
        #saveMessage(received_message)
        received_message = request.data
        saveMessage(received_message.decode("utf-8"))
        return "<p>Vastaanotettu.</p>"
    else:
        return render_template('404.html'), 404

# Tallennetaan vastaanotettu viesti JSON muodossa.
def saveMessage(message):
    newJson = {"message": message}
    with open("./data/messages.json", "r") as openMessages:
        loadMessages = json.load(openMessages)

    loadMessages["allMessages"].append(newJson) 

    with open("./data/messages.json", "w") as writeMessages:
       json.dump(loadMessages, writeMessages, indent=1, ensure_ascii=False)


# Palautetaan kaikki tallennetut viestit.
@app.route("/findmessage", methods=["GET"])
def findMessage():
    if request.method == "GET":
        f = open("./data/messages.json")
        data = json.load(f)
        f.close()
        return data
    else:
        return render_template('404.html'), 404

# Poistetaan kaikki viestit.
@app.route("/removemessage", methods=["POST"])
def removemessage():
    if request.method == "POST":
        cleanMessages = {"allMessages": [{"message": ""}]}
        with open("./data/messages.json", "w") as f:
            json.dump(cleanMessages, f)
        return "Viestit poistettu."
    else:
        return render_template('404.html'), 404

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
