import json
import os


def testi():
    newJson = {
    "message": "yay"
    }

    data = json.dumps(newJson)
    dir_list = os.listdir("./backend")
    print(dir_list)

    with open("./backend/messages.json", "r+") as f:
        load_data = json.load(f)
        print(load_data["allMessages"])


testi()