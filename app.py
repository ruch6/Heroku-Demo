# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:14:20 2021

@author: Ruchita
"""
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/predict", methods = ['POST'])
def predict():
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0],2)
    
    return render_template('index.html',prediction_text="Employee Salary should be $ {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)    