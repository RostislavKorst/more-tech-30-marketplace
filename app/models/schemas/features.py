from pydantic import BaseModel


class FeatureBase(BaseModel):
    name: str
    type: str


class FeatureCreate(FeatureBase):
    pass


class Feature(FeatureBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
