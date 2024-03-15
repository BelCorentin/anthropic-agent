from flask import Flask, jsonify, request
from agent.agent import AnthropicAgent

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        message = request.json.get('message')
    agent = AnthropicAgent()

    agent_response =  agent.ask(message)
    response = {'message': agent_response}
    print(response)

    json_response = jsonify(response)
    return json_response

if __name__ == '__main__':
    app.run()