import json
import os

FILE = "data/books.json"

def load_books():

    if not os.path.exists(FILE):
        return []

    with open(FILE, encoding="utf8") as f:
        return json.load(f)

def save_books(data):

    with open(FILE, "w", encoding="utf8") as f:
        json.dump(data, f, indent=4)
