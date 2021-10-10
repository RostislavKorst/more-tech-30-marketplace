from pydantic import BaseModel


class Partner(BaseModel):
    name: str
    description: str
