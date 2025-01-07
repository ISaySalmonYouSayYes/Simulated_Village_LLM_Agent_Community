from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from gpt.generate_persona import gpt4_generate_persona
from config import OPENAI_API_KEY, LANGSMITH_API_KEY

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
os.environ['LANGSMITH_API_KEY'] = LANGSMITH_API_KEY
app = Flask(__name__)
CORS(app)

# Define an API route
@app.route('/generate_persona', methods=['POST'])
def generate_persona():
    try:
        # Get the request data
        data = request.json
        name = data.get('name', None)

        if not name:
            return jsonify({"error": "Name is required"}), 400

        # Generate persona
        persona = gpt4_generate_persona(name)
        # return jsonify({"persona": persona})
        return jsonify(persona)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8964)

    #Usage, just copy and paste the bellowing code
    #curl -X POST http://127.0.0.1:8964/generate_persona -H "Content-Type: application/json" -d "{\"name\": \"John\"}"

