from pydantic import BaseModel
from typing import Union

class GreetMessage(BaseModel):
    message: str

class DataMessage(BaseModel):
    first_name: str
    middle_name: Union[str, None] = None
    last_name: str
    region: Union[str, None] = None
    city: str