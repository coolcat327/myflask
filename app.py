from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '1'


if __name__ == '__main__':
    app.run(debug=True)
