from flask import Flask, render_template, request, redirect, url_for, flash
import random
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DATA_FILE = 'quotes.json'

def load_quotes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_quote(new_quote):
    quotes = load_quotes()
    quotes.append(new_quote)
    with open(DATA_FILE, 'w') as f:
        json.dump(quotes, f, indent=4)

@app.route('/')
def quote():
    quotes = load_quotes()
    selected = random.choice(quotes)
    return render_template("quote.html", quote=selected["quote"], author=selected["author"])

@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        quote = request.form.get("quote")
        author = request.form.get("author")
        if quote and author:
            save_quote({"quote": quote, "author": author})
            flash("Quote submitted successfully!", "success")
            return redirect(url_for('quote'))
    return render_template("submit.html")

if __name__ == '__main__':
    app.run(debug=True)