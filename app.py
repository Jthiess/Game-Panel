from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Example card data that you can edit or replace with dynamic data
    middle_cards = [
        {'title': 'Middle Card 1', 'text': 'Some info about card 1'},
        {'title': 'Middle Card 2', 'text': 'Some info about card 2'},
        {'title': 'Middle Card 3', 'text': 'Some info about card 3'},
        {'title': 'Middle Card 4', 'text': 'Some info about card 4'},
    ]

    bottom_cards = [
        {'title': 'Bottom Card A', 'text': 'Details A'},
        {'title': 'Bottom Card B', 'text': 'Details B'},
        {'title': 'Bottom Card C', 'text': 'Details C'},
        {'title': 'Bottom Card D', 'text': 'Details D'},
    ]

    return render_template('index.html', middle_cards=middle_cards, bottom_cards=bottom_cards)

if __name__ == '__main__':
    app.run(debug=True)
