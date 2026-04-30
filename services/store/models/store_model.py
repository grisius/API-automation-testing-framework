from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class OrderStatus(str, Enum):

    placed = "placed"
    approved = "approved"
    delivered = "delivered"


class StoreModel(BaseModel):

    id: int | None = Field(default=None, ge=1, le=10)
    petId: int | None = None
    quantity: int | None = None
    shipDate: datetime | None = Field(default=None, alias="shipDate")
    status: OrderStatus | None = None
    complete: bool | None = None

