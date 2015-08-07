#!flask/bin/python
from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'])
def index():
    print('Received a call to fetch main page.')
    return app.send_static_file('index.html')


@app.route('/encode', methods=['POST'])
def encode():
    print('Received a call to encode.')
    print(request.json)
    return app.send_static_file('index.html')


@app.route('/<string:encoded>', methods=['GET'])
def decode(encoded):
    print('Received a call to decode string : ' + encoded)
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=18180, debug=True)
