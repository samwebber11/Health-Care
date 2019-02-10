#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 00:56:30 2019

@author: raghav
"""
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('final_template.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      sym1 = request.form.get('symptom 1')
      sym2 = request.form.get('symptom 2')
      sym3 = request.form.get('symptom 3')
      import model
      pred = model.prediction(sym1,sym2,sym3)
      return render_template("result.html",result =pred)
      #import model
      #ans=model.prediction(str)

if __name__ == '__main__':
   app.run(port=5000,debug = True)
