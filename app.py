from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Example card data that you can edit or replace with dynamic data
    middle_cards = [
        {'name': 'Game Server 1', 'motd': 'motd1', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
        {'name': 'Game Server 2', 'motd': 'motd2', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
        {'name': 'Game Server 3', 'motd': 'motd3', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
        {'name': 'Game Server 4', 'motd': 'motd4', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
        {'name': 'Game Server 5', 'motd': 'motd5', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
        {'name': 'Game Server 6', 'motd': 'motd6', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
        {'name': 'Game Server 7', 'motd': 'motd7', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
        {'name': 'Game Server 8', 'motd': 'motd8', 'online': True, 'game': 'Minecraft', 'playing_now': 12, 'playing_max': 20, "version": "1.8.9", "description": "A fun Minecraft server"},
    ]

    bottom_cards = [
        {'title': 'Bottom Card A', 'text': 'Details A'},
        {'title': 'Bottom Card B', 'text': 'Details B'},
        {'title': 'Bottom Card C', 'text': 'Details C'},
        {'title': 'Bottom Card D', 'text': 'Details D'},
        {'title': 'Bottom Card E', 'text': 'Details E'},
        {'title': 'Bottom Card F', 'text': 'Details F'},
        {'title': 'Bottom Card G', 'text': 'Details G'},
        {'title': 'Bottom Card H', 'text': 'Details H'},
    ]

    return render_template('index.html', middle_cards=middle_cards, bottom_cards=bottom_cards)

if __name__ == '__main__':
    app.run(debug=True)
