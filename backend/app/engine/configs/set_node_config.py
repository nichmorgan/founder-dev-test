from typing import Any

from pydantic import BaseModel


class SetNodeConfig(BaseModel):
    path: str = ""
    value: Any
