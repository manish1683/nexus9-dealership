"""
schemas.py
----------
Pydantic models for request and response validation.
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Car(BaseModel):
    id: str
    model: str
    tagline: str
    engine: str
    top_speed_kmh: int
    price_mega_credits: float
    image_url: str
    gallery_images: List[str] = []
    hp: int = 1500
    acceleration_sec: float = 1.8
    range_km: int = 750
    detailed_features: List[str] = []
    icon: str
    icon_color: str
    stock: int


class OrderCreate(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    phone: str = Field(..., min_length=6, max_length=20)
    car_id: str
    quantity: int = Field(1, ge=1, le=10)
    notes: Optional[str] = Field(None, max_length=500)


class OrderOut(BaseModel):
    id: int
    customer_name: str
    email: str
    phone: str
    car_id: str
    car_model: str
    quantity: int
    unit_price: float
    total_price: float
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Existing Order schemas ke neeche ye add karein:
class ContactCreate(BaseModel):
    name: str
    email: str
    message: str

class ContactOut(BaseModel):
    id: int
    name: str
    email: str
    message: str
    created_at: datetime

    class Config:
        from_attributes = True