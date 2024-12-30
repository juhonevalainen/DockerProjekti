import json

def saveMessage(message):
    newJson = {"message": message}
    with open("./backend/kokeilu.json", "r+") as f:
        load_data = json.load(f)
        load_data["allMessages"].append(newJson)
        f.seek(0)
        json.dump(load_data, f, indent=1)

def findMessage():
    f = open("./backend/kokeilu.json")
    data = json.load(f)
    f.close()
    return json.dumps(data)


saveMessage("Tämä on ääkköstesti.")
print(findMessage())

#{
# "allMessages": [
#
# ]
#}