from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db import crud
from app.db.database import get_db
from app.models.schemas.datasets import DatasetsInResponse, DatasetCreate, Dataset
from app.models.schemas.features import Feature, FeatureCreate

router = APIRouter()


@router.post("", response_model=Dataset, name="Add dataset to database")
def add_new_dataset(dataset: DatasetCreate, db: Session = Depends(get_db)):
    db_dataset = crud.get_dataset_by_name(db, name=dataset.name)
    if db_dataset:
        raise HTTPException(status_code=400, detail="Dataset with this name already in DataBase")
    return crud.create_dataset(db=db, dataset=dataset)


@router.get("", response_model=DatasetsInResponse, name="Returns all datasets names")
def get_datasets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_datasets(db, skip=skip, limit=limit)
    return DatasetsInResponse(datasets=items)


@router.post("/{dataset_id}/columns/", response_model=Feature, name="Add column for dataset by id")
def create_feature_for_dataset(dataset_id: int, feature: FeatureCreate, db: Session = Depends(get_db)):
    db_feature = crud.get_feature_by_dataset(db, dataset_id=dataset_id, feature_name=feature.name)
    if db_feature:
        raise HTTPException(status_code=400, detail="Column with this name already in dataset")
    return crud.create_dataset_feature(db=db, feature=feature, dataset_id=dataset_id)
