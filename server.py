from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from llm import generate_random_japanese_sentence, generate_response, generate_business_japanese_translation
app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/', methods=['POST'])
def hello_world():
    response_text = generate_response(generate_random_japanese_sentence())
    
    # Return the response from generate_response
    return jsonify(message=response_text)

@app.route('/health', methods=['GET'])
def health():
    return "OK"

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

@app.route('/hello', methods=['GET'])
def hello():
    # Get the English text from query parameter
    english_text = request.args.get('text', '')
    
    # Generate business Japanese translation
    response_text = generate_business_japanese_translation(english_text)
    
    # Return the response
    return jsonify(message=response_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)