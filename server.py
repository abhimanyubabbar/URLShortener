#!flask/bin/python
from flask import Flask, jsonify, redirect
from flask import request
from shortener.shorten import UrlShortener

app = Flask(__name__, static_url_path='')
shortener = UrlShortener()


@app.route('/', methods=['GET'])
def index():
    print('Received a call to fetch main page.')
    return app.send_static_file('index.html')


@app.route('/encode', methods=['POST'])
def encode():
    print('Received a call to encode.')
    print(request.json)
    url = shortener.shortenUrl(request.json['url'])
    print('Shortened Url:' + url)
    return jsonify({'url': url}), 201


@app.route('/<string:encoded>', methods=['GET'])
def decode(encoded):
    print('Received a call to decode string : ' + encoded)
    originalUrl = shortener.originalUrl(encoded)
    print("Original Url:" + originalUrl)
    return redirect(originalUrl, code=301)

if __name__ == '__main__':
    app.run(port=18180, debug=True)
