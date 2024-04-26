from flask import Flask, request, jsonify
from flask_cors import CORS
from g4f.client import Client

# Create the Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define a route for the GPT-3.5-turbo chat
@app.route('/gpt-chat', methods=['POST'])
def gpt_chat():
    # Get the JSON data from the request
    data = request.get_json()

    # Validate the data and ensure 'message' is provided
    if 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400

    # Create a Client instance and get the response from GPT-3.5-turbo
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": data['message']}]
    )

    # Return the response content as JSON
    response_content = response.choices[0].message.content
    return jsonify({'response': response_content})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
