import os
import math
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    version = os.environ.get('SERVICE_VERSION')

    # do some cpu intensive computation
    x = 0.0001
    for i in range(0, 1000000):
        x = x + math.sqrt(x)

    return 'Hello, I am Store service version: %s' % (version)


@app.route('/health')
def health():
    return 'store is healthy', 200


if __name__ == "__main__":
    app.run(host='::', threaded=True)