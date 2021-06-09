from flask import Flask, request, jsonify

app = Flask(__name__)

prices = {
    'food': {
        'Margherita': 11.75,
        'Vegetariana': 12.50,
        'Diavola': 13.25
    },
    'drinks': {
        'Strongbow': 2.50,
        'Stella Artois': 3.50,
        'Prosecco': 6.50
    }
}

@app.route('/post/order', methods=['POST'])
def post_order():
    food = request.json['food']
    drink = request.json['drink']

    price = prices['food'][food] + prices['drinks'][drink]
    price *= 1.1 # service charge
    price = round(price, 2)

    return jsonify(price) # we use jsonify to send numbers

if __name__ == '__main__':
    app.run(host='0.0.0.0')