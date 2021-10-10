from fastapi import APIRouter

from app.models.schemas.datasets import DatasetsInResponse
from app.models.schemas.partners import PartnersInResponse

router = APIRouter()


@router.post("", response_model=PartnersInResponse, name="Add dataset to cart")
async def add_to_cart():
    pass


@router.delete("/", response_model=DatasetsInResponse, name="Delete dataset from cart by dataset Id")
async def delete_from_cart(partner: str):
    pass
