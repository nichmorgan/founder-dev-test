from pydantic import BaseModel, Field


class StartNodeConfig(BaseModel):
    input_path: str = Field(default="", alias="inputPath")
