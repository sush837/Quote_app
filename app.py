from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Make it work, make it right, make it fast.",
    "Simplicity is the soul of efficiency."
]

@app.route('/')
def home():
    return jsonify({
        'quote': random.choice(quotes)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

