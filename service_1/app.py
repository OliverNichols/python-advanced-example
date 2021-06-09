from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    food = requests.get('http://service-2:5000/get/food').text # m.get('http://service-2:5000/get/food', text='Margherita')
    drink = requests.get('http://service-3:5000/get/drink').text # m.get('http://service-3:5000/get/drink', text='Stella Artois')

    payload = {'food': food, 'drink': drink}
    price = requests.post('http://service-4:5000/post/order', json=payload).json() # m.post('http://service-4:5000/post/order', json=7.50)

    return f"You ordered a {food} and a {drink} for £{price}.\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')