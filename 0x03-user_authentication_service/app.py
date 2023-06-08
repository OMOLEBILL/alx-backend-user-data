#!/usr/bin/env python3
"""We serve the app"""
from flask import Flask, jsonify
from os import getenv

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def Home():
    """The place that i would got to"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
