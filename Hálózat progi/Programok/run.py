
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"Message": "Fine"})

if __name__ == '__main__':
    app.run()