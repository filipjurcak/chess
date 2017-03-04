from flask import Flask, jsonify
from Classes.Game import Game
import json

app = Flask(__name__)


@app.route("/")
def hello():
    hra = Game()
    with open("ja.json", "w") as outfile:
        json.dump({str(len(hra.figures))}, outfile)
    for i in range(len(hra.figures)):
        with open("ja.json", "w") as outfile:
            json.dump({'name': str(hra.figures[i].__class__.__name__), 'color': str(hra.figures[i].color),
                   'x': hra.figures[i].a, 'y': hra.figures[i].b}, outfile)
    with open("ja.json", 'w') as outfile:
        json.dump({str(hra.whomoves)}, outfile)
    with open('ja.json') as json_data:
        data = json.load(json_data)
    e = jsonify(data)
    return e

if __name__ == "__main__":
    app.run()
