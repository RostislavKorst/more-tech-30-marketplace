from fastapi import APIRouter

from app.models.schemas.datasets import DatasetsInResponse
from app.models.schemas.partners import PartnersInResponse

router = APIRouter()


@router.post("", response_model=PartnersInResponse, name="Add step of given type")
async def add_step():
    pass


@router.delete("/", response_model=DatasetsInResponse, name="Delete step by step id")
async def delete_from_cart(partner: str):
    pass
