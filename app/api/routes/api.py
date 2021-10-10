from fastapi import APIRouter

from app.api.routes import cart, steps, datasets

router = APIRouter()
router.include_router(datasets.router, tags=["datasets"], prefix="/datasets")
router.include_router(cart.router, tags=["cart"], prefix="/cart")
router.include_router(steps.router, tags=["steps"], prefix="/steps")
