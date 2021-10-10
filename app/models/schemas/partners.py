from typing import List

from pydantic import BaseModel

from app.models.domain.partners import Partner


class PartnersInResponse(BaseModel):
    partners: List[Partner]
