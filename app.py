from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# List of silly responses
SILLY_RESPONSES = [
    "That sounds about as smart as a screen door on a submarine.",
    "I've seen better ideas from a sleepwalking hamster.",
    "That's not even wrong - it's creatively incorrect!",
    "If stupidity was a superpower, you'd be invincible.",
    "I'd agree with you but then we'd both be wrong.",
    "That idea is so bad it's circling back to almost good.",
    "Did you have a brain fart or is this your normal thinking?",
    "I'd explain why you're wrong but I don't have any crayons with me.",
    "That's the kind of idea that makes horoscopes look scientific.",
    "Congratulations! You've invented a new way to be wrong."
]

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        response.headers.add('Access-Control-Allow-Methods', '*')
        return response
    
    data = request.get_json()
    random_response = random.choice(SILLY_RESPONSES)
    response = jsonify({'prediction': random_response})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)