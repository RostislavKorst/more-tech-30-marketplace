from sqlalchemy.orm import Session

import app.models.schemas.datasets
import app.models.schemas.features
from app.db import models


def create_dataset(db: Session, dataset: app.models.schemas.datasets.DatasetCreate):
    db_dataset = models.Dataset(name=dataset.name)
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset


def create_dataset_feature(db: Session, feature: app.models.schemas.features.FeatureCreate, dataset_id: int):
    db_feature = models.Feature(**feature.dict(), owner_id=dataset_id)
    db.add(db_feature)
    db.commit()
    db.refresh(db_feature)
    return db_feature


def get_datasets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dataset).offset(skip).limit(limit).all()


def get_dataset_by_name(db: Session, name: str):
    return db.query(models.Dataset).filter(models.Dataset.name == name).first()


def get_feature_by_dataset(db: Session, dataset_id: int, feature_name: str):
    return db.query(models.Feature) \
        .filter(models.Feature.owner_id == dataset_id) \
        .filter(models.Feature.name == feature_name).first()
