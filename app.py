from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of motivational quotes
quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don't let yesterday take up too much of today.",
    "You learn more from failure than from success.",
    "It's not whether you get knocked down, it's whether you get up.",
]

@app.route('/quote', methods=['GET'])
def get_quote():
    """Returns a random quote."""
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)