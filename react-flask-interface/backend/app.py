from flask import Flask, jsonify, request
from agent import AnthropicAgent

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        message = request.json.get('message')
    agent = AnthropicAgent()

    data = {'message': agent.ask(message)}

    return jsonify(data)

if __name__ == '__main__':
    app.run()