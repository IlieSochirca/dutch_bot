"""This Module is parsing a PDF file with PyPDF2"""
import json

entry = dict()
entry_keys = ["dutch", "english", "part_of_speech"]

with open("nl-en-dict.txt") as file_handler:
    for line in file_handler:
        formatted_line = []
        if not line.startswith("#"):
            with open("dictionary_database.json", "r+") as json_handler:
                entry.update(zip(entry_keys, line.strip().split("\t")))
                data = json.load(json_handler)
                data.append(entry)
                json_handler.seek(0)
                json.dump(data, json_handler)
