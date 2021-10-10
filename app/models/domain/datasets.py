from typing import List

from pydantic import BaseModel

from app.models.domain.columns import Column


class Dataset(BaseModel):
    name: str
    columns: List[Column]

    class Config:
        orm_mode = True
