import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

application = Flask(__name__) #Initialize the flask App

@application.route('/')
def home():
    return render_template('mapa_premios_oscar.html')

if __name__ == "__main__":
    application.run(debug=True)
