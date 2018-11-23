from flask import Flask, jsonify, request
import logging
from image_classify.classify_api import classify

app = Flask(__name__)
URL_PREFIX = '/cifar-service'

@app.route(URL_PREFIX + "/")
def index():
    return "v1"


@app.route(URL_PREFIX + '/classify', methods=['POST'])
def cls():
    if request.files.get('file'):
        file = request.files.get('file')
        data = file.read()
        return jsonify({'result': classify(data)})
    else:
        return index()

if __name__ == '__main__':
    app.run(debug=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
