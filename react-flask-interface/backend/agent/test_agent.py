"""
Small testing script for the agent
"""

import anthropic
from agent import AnthropicAgent

def test_agent_initialization():
    agent = AnthropicAgent(name="test", style="Pirate Style")
    assert agent.name == "test"
    assert agent.style == "Pirate Style"

def test_agent_initialization_no_style():
    agent = AnthropicAgent(name="test")
    assert agent.name == "test"
    assert agent.style == "Normal Style"

def test_agent_initialization_no_name():
    agent = AnthropicAgent(style="Pirate Style")
    assert agent.name == "No Name"
    assert agent.style == "Pirate Style"

def test_agent_ask():
    agent = AnthropicAgent(name="test")
    response = agent.ask("Hello")
    print(response)
    assert response is not None