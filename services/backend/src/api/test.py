import json

with open("./dictionary_database.json") as fh:
    print(json.load(fh))