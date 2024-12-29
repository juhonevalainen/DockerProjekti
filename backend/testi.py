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
        # Katsotaan onko tiedosto täysin tyhjä.
        #if len(load_data) == 0:
        #    load_data = {"allMessages": []}
        load_data["allMessages"].append(newJson)
        print(load_data)


testi()