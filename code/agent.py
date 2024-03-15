"""
Agent class for the anthropic agent
"""

from pydantic import BaseModel
from typing import List, Optional

class AnthropicAgent(BaseModel):
    name: str
    style: str
