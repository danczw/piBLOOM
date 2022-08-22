from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve

import logging
logging.basicConfig(
    encoding='utf-8',
    level=logging.DEBUG,
    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)

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
    
    app.logger.info(
        f'request {request.remote_addr} {request.path} {request.method} : response {response.status}'
    )
    
    return response

@app.route('/chat/', methods=['POST'])
def chat_with_bot():
    content = request.json['content']
    answer = bloom.predict(content=content)

    response = jsonify({'data': answer[0]['generated_text']})
    
    app.logger.info(
        f'request {request.remote_addr} {request.path} {request.method} : response {response.status}'
    )

    return response

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)