"""
Agent class for the anthropic agent
"""

import anthropic
from pydantic import BaseModel
from typing import Any, List, Optional

class AnthropicAgent(BaseModel):
    # Setting defaults for the agent
    name: str = "No Name"
    style: str = "Normal Style"
    client: anthropic.Anthropic = anthropic.Anthropic()


    class Config:
        arbitrary_types_allowed = True

    # Defining a ask function, which queries the Anthropic API
    def ask(self, message: str) -> str:

        with self.client.messages.stream(
            max_tokens=1024,
            messages=[{"role": "user", "content": message}],
            model="claude-3-opus-20240229",
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)
        return text
        
