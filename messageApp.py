from flask import Flask, jsonify, request
app = Flask(__name__)

messages = []

@app.route("/message", methods=["GET", "POST"])
def hello_world():
    resp = {
        "Allmessage":messages
    }
    if request.method == "GET":
        resp["Allmessage"] = messages
    else:
        message = request.json["message"]
        messages.append(message)
        resp["Allmessage"] = messages
    return jsonify(resp)
