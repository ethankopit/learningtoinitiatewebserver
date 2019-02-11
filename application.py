from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('betterindex.html')

@app.route('/motherfuckingwebsite.com')
def linkedpage():
    return render_template('motherfuckingwebsite.html')

