import argparse
from agent import AnthropicAgent

def main():
    parser = argparse.ArgumentParser(description='Anthropic Agent')
    parser.add_argument('--name', default='No Name', help='Name of the agent')
    parser.add_argument('--style', default='Normal Style', help='Style of the agent')
    parser.add_argument('--message', default='Hello', help='Message to ask the agent')

    args = parser.parse_args()

    agent = AnthropicAgent(name=args.name, style=args.style)
    response = agent.ask(args.message)

    print(response)

if __name__ == '__main__':
    main()