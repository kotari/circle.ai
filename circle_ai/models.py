from typing import List, Optional

from pydantic import BaseModel

class GenerateInput(BaseModel):
    model: str
    prompt: str
    stream: bool
    parameters: dict