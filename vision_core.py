from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "<h1>Cancan Kern: AI Vision Core</h1><p>Status: OPERATIONAL</p>"

@app.route('/analyze')
def analyze():
    return jsonify({
        "status": "active",
        "taxonomy": "Polymer > PET #1 > Soiled",
        "digital_twin": "Active"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
