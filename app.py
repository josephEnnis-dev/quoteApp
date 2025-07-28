from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    {"quote": "Keep going. Everything you need will come to you at the perfect time.", "author": "Unknown"},
    {"quote": "Do something today that your future self will thank you for.", "author": "Sean Patrick Flanery"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan"}
]

@app.route('/')
def quote():
    selected = random.choice(quotes)
    return render_template("quote.html", quote=selected["quote"], author=selected["author"])

if __name__ == '__main__':
    app.run(debug=True)