from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():

    data = 'Could not load HTML :('

    with open('index.html', 'r') as html:
        data = html.read()

    return data
