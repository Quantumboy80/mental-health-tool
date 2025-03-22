from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# List of words for sentiment analysis
POSITIVE_WORDS = ["happy", "joyful", "excited", "content", "grateful"]
NEGATIVE_WORDS = ["sad", "depressed", "anxious", "stressed", "overwhelmed", "unhappy", "worried"]

@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json  # Get JSON data from request
    
    # Extract parameters
    text = data.get("text", "").lower()
    sleep_hours = data.get("sleep_hours", 0)
    water_intake = data.get("water_intake", 0)

    # Determine emotion
    emotion = "NEUTRAL"
    recommendation = "Keep monitoring your mood."

    if any(word in text for word in POSITIVE_WORDS):
        emotion = "POSITIVE"
        recommendation = "Great! Keep engaging in positive habits!"
    elif any(word in text for word in NEGATIVE_WORDS):
        emotion = "NEGATIVE"
        recommendation = "Consider talking to a friend, journaling, or seeking professional help."

    # Additional health recommendations
    if sleep_hours < 6:
        recommendation += " Try to get at least 7-8 hours of sleep."
    if water_intake < 2:
        recommendation += " Drink more water (aim for at least 2L per day)."

    return jsonify({
        "emotion": emotion,
        "recommendation": recommendation,
        "score": 0.8,  # Dummy score for now
        "sleep_hours": sleep_hours,
        "water_intake": water_intake
    })

if __name__ == "__main__":
    app.run(debug=True)
