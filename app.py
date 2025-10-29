from flask import Flask, render_template, jsonify
import os
import json
import random

app = Flask(__name__)


def get_card_image(name):
    """Convert card name to an image path, falling back to default if image doesn't exist."""
    # Convert name to lowercase and replace spaces with hyphens for the filename
    image_name = (name).lower().replace(' ', '-') + '.jpg'
    # Resolve path relative to this file so existence checks work reliably
    image_path = os.path.join(os.path.dirname(__file__), 'static', 'images', 'cards', image_name)
    if os.path.exists(image_path) and image_name.strip() != '.jpg':
        return f'/static/images/cards/{image_name}'
    return '/static/images/cards/default.jpg'


def _data_file_path():
    return os.path.join(os.path.dirname(__file__), 'data', 'cards.json')


def load_cards():
    """Read card data from data/cards.json and resolve image paths for each card."""
    path = _data_file_path()
    if not os.path.exists(path):
        return {'middle_cards': [], 'bottom_cards': []}
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    middle = data.get('middle_cards', [])
    bottom = data.get('bottom_cards', [])

    # Ensure each card has a resolved image path
    for card in middle + bottom:
        if not card.get('image'):
            card['image'] = get_card_image(card.get('game', '')).lower()

    return {'middle_cards': middle, 'bottom_cards': bottom}


def get_random_message():
    """Read and return a random message from the messages.txt file."""
    message_path = os.path.join(os.path.dirname(__file__), 'data', 'messages.txt')
    if not os.path.exists(message_path):
        return "Welcome to Game Panel!"
    with open(message_path, 'r', encoding='utf-8') as f:
        messages = f.read().splitlines()
    return random.choice(messages) if messages else "Welcome to Game Panel!"

@app.route('/')
def index():
    cards = load_cards()
    random_message = get_random_message()
    # Keep server-side render initially using the JSON source (works if JS is disabled)
    return render_template('index.html', 
                         middle_cards=cards['middle_cards'], 
                         bottom_cards=cards['bottom_cards'],
                         random_message=random_message)


@app.route('/api/cards')
def api_cards():
    """Return card data as JSON. External tools can edit the JSON file later and this endpoint will reflect changes."""
    return jsonify(load_cards())

if __name__ == '__main__':
    app.run(debug=True)
