from typing import List

from pydantic import BaseModel

from app.models.schemas.features import Feature


class DatasetBase(BaseModel):
    name: str


class DatasetCreate(DatasetBase):
    pass


class Dataset(DatasetBase):
    id: int
    columns: List[Feature] = []

    class Config:
        orm_mode = True


class DatasetNamesInResponse(BaseModel):
    datasets: List[Dataset] = []


class DatasetsInResponse(BaseModel):
    datasets: List[Dataset] = []
