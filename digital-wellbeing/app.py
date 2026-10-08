from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    screen = float(data['screen_time'])
    social = float(data['social_media'])
    sleep = float(data['sleep_hours'])
    unlock = float(data['unlocks'])

    # Simple logic (replace with ML later)
    score = screen + social + unlock/50 - sleep

    if score > 15:
        risk = 2
        stress = "High"
    elif score > 8:
        risk = 1
        stress = "Medium"
    else:
        risk = 0
        stress = "Low"

    return jsonify({
        "risk_level": risk,
        "stress": stress
    })

if __name__ == '__main__':
    app.run(debug=True)