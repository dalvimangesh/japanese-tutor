from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from llm import generate_response
app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/', methods=['POST'])
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/submit', methods=['POST'])
def submit_text():
    data = request.json
    text = data.get('text', '')
    
    # Pass the text to generate_response function
    response_text = generate_response(text)
    
    # Return the response from generate_response
    return jsonify(message=response_text)

@app.route('/styles.css', methods=['GET'])
def serve_css():
    return send_from_directory('.', 'styles.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)