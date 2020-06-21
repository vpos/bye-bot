import flask
import bye as Cheems
import traceback
import re

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

@app.route('/quits', methods=['POST'])
def quits():
    log_request_info()

    requestString = str(request.get_data())
    name_extracted = ''
    text_extracted = ''
    try:
        name_extracted = re.search(r'user_name=(.+?)&', requestString, re.IGNORECASE).group(1)
    except:
        traceback.print_exc()
        pass

    try:
        text_extracted = re.search(r'text=%22(.+?)%', requestString, re.IGNORECASE).group(1)
        text_extracted = text_extracted.replace("+", " ")
    except:
        traceback.print_exc()
        pass
    
    return Cheems.quits(name_extracted, text_extracted)

app.run()