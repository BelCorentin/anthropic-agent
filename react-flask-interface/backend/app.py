from flask import Flask, jsonify, request
from agent.agent import AnthropicAgent

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        message = request.json.get('message')
    agent = AnthropicAgent()

    response =  agent.ask(message)
    data = {'message': response}
    print(response)

    return jsonify(data)

if __name__ == '__main__':
    app.run()