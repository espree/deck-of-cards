from flask import Flask, jsonify, request
import CardDeck, random

app = Flask(__name__)

deck_of_cards = []

@app.route('/', methods=['GET', 'POST'])
def index():
   if (request.method == 'POST'):
      some_json = request.get_json()
      return jsonify({'you sent': some_json}), 201
   else:
      return jsonify({"about":"HelloWorld"})

#Draws a card
@app.route('/draw', methods=['GET'])
def draw():
    if len(deck_of_cards) > 0:
        return jsonify(deck_of_cards.pop(0))
    else:
        return jsonify(('No', 'cards'))

#Shuffles a new deck, returns nothing back from deck so send a message
@app.route('/shuffle', methods=['GET'])
def shuffle():
    deck_of_cards.clear()
    deck_of_cards.extend(CardDeck.carddeck)
    random.shuffle(deck_of_cards)
    return jsonify({"message": len(deck_of_cards)})

@app.route('/count', methods=['GET'])
def count():
    return jsonify(('Count', len(deck_of_cards)))

#Puts a card back to the bottom of the deck
#@app.route('/return', methods=['POST'])
#def return_card()
#    card = request.get_json()
#    deck_of_cards.append((card.face, card.suit))
