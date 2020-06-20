import flask
import bye as Cheems

from flask import request


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.before_request
def log_request_info():
    print('Headers: %s', request.headers)
    print('Body: %s', request.get_data())

@app.route('/', methods=['GET'])
def home():
    return 'Pong'

@app.route('/qit', methods=['POST'])
def home():
    log_request_info
    return Cheems.quits()

app.run()