from flask import Flask, jsonify, request
from flask_cors import CORS

# handle import via poetry initialization and python
try:
    from pibloom.model import bloom_model
except ImportError:
    from model import bloom_model

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) # TODO: add origin restriction

bloom = bloom_model()

@app.route('/index/', methods=['GET'])
def index():
    response = jsonify({'data': 'Hello World!'})
        
    return response

@app.route('/chat/', methods=['POST'])
def chat_with_bot():
    content = request.json['content']
    answer = bloom.predict(content=content)

    response = jsonify({'data': answer[0]['generated_text']})

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)