from flask import Flask, render_template
import requests

PORT = 8000 # usual port for HTTP
HOST = '0.0.0.0' # localhost
DB_URL = "http://localhost:5000"

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/info")
def get_info():
    r = requests.get(DB_URL + "/info")
    return render_template('info.html', body=r.text)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)