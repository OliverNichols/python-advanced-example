from flask import Flask
import random

app = Flask(__name__)

food = ['Margherita', 'Vegetariana', 'Diavola']

@app.route('/get/food')
def get_food():
    return random.choice(food)

if __name__ == '__main__':
    app.run(host='0.0.0.0')