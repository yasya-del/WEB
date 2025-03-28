from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
        return '''[
    ["illusion", "Telepathy", "telekinesis"],
    ["invisibility", "copies", "chameleon", "Teleportation"],
    ["Space warping", "space cycling"],
    ["Time cycling", "transformation", "Rebirth"],
    ["fireballs", "Default"]
]'''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)