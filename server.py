#!venv/bin/python
import os
from flask import Flask, jsonify, redirect, abort
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
    url = shortener.shorten_url(request.json['url'])
    print('Shortened Url:' + url)
    return jsonify({'url': url}), 201


@app.route('/<string:encoded>', methods=['GET'])
def decode(encoded):
    print('Received a call to decode string : ' + encoded)
    original_url = shortener.original_url(encoded)

    if original_url == '':
        return abort(404)

    print("Original Url:" + original_url)
    return redirect(original_url, code=301)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
