import json
def read():
    with open("config.json", "r") as file:
        data = json.loads(file.read())
    return data