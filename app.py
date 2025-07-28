import random

quotes = [
    {"quote": "Keep going. Everything you need will come to you at the perfect time.", "author": "Unknown"},
    {"quote": "Do something today that your future self will thank you for.", "author": "Sean Patrick Flanery"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan"}
]

selected = random.choice(quotes)
print("💡 Quote of the Day:")
print(f"{selected['quote']} — {selected['author']}")