from flask import Flask, jsonify, request
from image_classify.classify_api import classify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/classify', methods=['POST'])
def cls():
    if request.files.get('file'):
        file = request.files.get('file')
        data = file.read()
        return jsonify({'result': classify(data)})
    else:
        return index()

if __name__ == '__main__':
    app.run(debug=True)
