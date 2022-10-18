from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    response = "Hello, World!"
    return jsonify(response)

@app.route("/api/tags")
def hello_world():
    response = "Hello, World!"
    return jsonify(response)