from enum import Enum
from typing import Any
from pydantic import BaseModel


class IfOperator(str, Enum):
    eq = "="
    lt = "<"
    lte = "<="
    gt = ">"
    gte = ">="


class IfNodeConfig(BaseModel):
    path: str = ""
    operator: IfOperator
    value: Any
