# Python http test server
# A simple it works page to test network connectivity
# Github: https://www.github.com/0x4248/Python_http_test_server
# By: 0x4248

from flask import Flask, render_template, request, redirect, url_for, flash

PORT = 80

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)