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
    client: anthropic.Client = None

    class Config:
        arbitrary_types_allowed = True

    # Defining a ask function, which queries the Anthropic API
    def ask(self, message: str) -> str:
        
        self.client = anthropic.Client()
        # Streaming
        # with self.client.messages.stream(
        #     max_tokens=1024,
        #     messages=[{"role": "user", "content": message}],
        #     model="claude-3-opus-20240229",
        # ) as stream:
        #     for text in stream.text_stream:
        #         print(text, end="", flush=True)
        #         # yield text

        # Simple text completion
        response = anthropic.Anthropic().messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.content[0].text
        