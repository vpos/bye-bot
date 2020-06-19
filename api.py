import flask
import bye as Cheems

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return Cheems.quits()

app.run()