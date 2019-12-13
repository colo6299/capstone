from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    return render_template("index.html")               

@app.route('/buy')
def buy():
    '''return buy page'''
    return render_template("buy.html")

@app.route('/sell')
def sell():
    '''return sell page'''
    return render_template("sell.html")


if __name__ == '__main__':
    app.run(debug=True)

