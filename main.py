from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/', methods=["POST"])
def handling_post():
    return 'Rauf master'


if __name__ == '__main__':
    app.run()