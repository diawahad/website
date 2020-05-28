# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:12:56 2019

@author: sdiaw
"""

from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

#if __name__ == "__main__":
#    app.run()