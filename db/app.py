from flask import Flask, jsonify

PORT = 5000 # usual port for HTTP
HOST = '0.0.0.0' # localhost

app = Flask(__name__)

@app.route("/info")
def hello():
    data = {
        "info": "This is returning something from a different container!"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)