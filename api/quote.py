from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app) # Enables the frontend to access this backend

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "It always seems impossible until it is done. - Nelson Mandela",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Code is like humor. When you have to explain it, it’s bad. - Cory House",
    "First, solve the problem. Then, write the code. - John Johnson",
    "Experience is the name everyone gives to their mistakes. - Oscar Wilde",
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "Energy and persistence conquer all things. - Benjamin Franklin",
    "It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change. - Charles Darwin",
    "Programming isn't about what you know; it's about what you can figure out. - Chris Pine",
    "The mind is everything. What you think you become. - Buddha",
    "Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence. - Helen Keller",
    "What we know is a drop, what we don't know is an ocean. - Isaac Newton",
    "Simplicity is the soul of efficiency. - Austin Freeman",
    "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "A person who never made a mistake never tried anything new. - Albert Einstein",
    "Act as if what you do makes a difference. It does. - William James",
    "Happiness depends upon ourselves. - Aristotle",
    "Nature is not mute, it is man who is deaf. - Terence McKenna",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "Fall seven times and stand up eight. - Japanese Proverb",
    "If you can dream it, you can do it. - Walt Disney",
    "Make each day your masterpiece. - John Wooden",
    "Imagination is more important than knowledge. - Albert Einstein",
    "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs"
]
    return jsonify({'quote': random.choice(quotes)})

app = app

if __name__ == '__main__':
    app.run(debug=True)