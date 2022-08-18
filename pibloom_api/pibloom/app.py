from flask import Flask, jsonify, request

# handle import via poetry initialization and python
try:
    from pibloom.model import bloom_model
except ImportError:
    from model import bloom_model

app = Flask(__name__)

@app.route('/index/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello World!'})

@app.route('/chat/', methods=['POST'])
def chat_with_bot():
    content = request.json['content']
    bloom = bloom_model()
    
    answer = bloom.predict(content=content)

    return jsonify({'data': answer[0]['generated_text']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)