from flask import Flask
import random

app = Flask(__name__)

drinks = ['Strongbow', 'Stella Artois', 'Prosecco']

@app.route('/get/drink')
def get_drink():
    return random.choice(drinks)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')