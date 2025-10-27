from flask import Flask, render_template

app = Flask(__name__)

def get_card_image(name):
    """Convert card name to an image path, falling back to default if image doesn't exist"""
    import os
    # Convert name to lowercase and replace spaces with hyphens for the filename
    image_name = name.lower().replace(' ', '-') + '.jpg'
    image_path = os.path.join('static', 'images', 'cards', image_name)
    # Check if the image exists, otherwise return a default
    if os.path.exists(image_path):
        return f'/static/images/cards/{image_name}'
    return '/static/images/cards/default.jpg'

@app.route('/')
def index():
    # Example card data that you can edit or replace with dynamic data
    middle_cards = [
        {'name': 'Game Server 1', 'motd': 'motd1', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('minecraft')},
        {'name': 'Game Server 2', 'motd': 'motd2', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('')},
        {'name': 'Game Server 3', 'motd': 'motd3', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('')},
        {'name': 'Game Server 4', 'motd': 'motd4', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('')},
        {'name': 'Game Server 5', 'motd': 'motd5', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('')},
        {'name': 'Game Server 6', 'motd': 'motd6', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('')},
        {'name': 'Game Server 7', 'motd': 'motd7', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('')},
        {'name': 'Game Server 8', 'motd': 'motd8', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server", 'image': get_card_image('')},
    ]

    bottom_cards = [
        {'name': 'Bottom Card A', 'game': 'Details A', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': 'BottomA description', 'image': get_card_image('testing')},
        {'name': 'Bottom Card B', 'game': 'Details B', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': 'BottomB description', 'image': get_card_image('testing')},
        {'name': 'Bottom Card C', 'game': 'Details C', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': 'BottomC description', 'image': get_card_image('testing')},
        {'name': 'Bottom Card D', 'game': 'Details D', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': 'BottomD description', 'image': get_card_image('testing')},
        {'name': 'Bottom Card E', 'game': 'Details E', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': 'BottomE description', 'image': get_card_image('testing')},
        {'name': 'Bottom Card F', 'game': 'Details F', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': "BottomF description", 'image': get_card_image('testing')},
        {'name': 'Bottom Card G', 'game': 'Details G', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': "BottomG description", 'image': get_card_image('testing')},
        {'name': 'Bottom Card H', 'game': 'Details H', 'version': '1.8.9', 'file_size': '150MB', 'retirement_date': '2025-12-31', 'description': "BottomH description", 'image': get_card_image('testing')},
    ]

    return render_template('index.html', middle_cards=middle_cards, bottom_cards=bottom_cards)

if __name__ == '__main__':
    app.run(debug=True)
