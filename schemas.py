from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class VendorBase(BaseModel):
    name: str
    category: str
    location_city: Optional[str] = None
    location_state: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    rating: Optional[float] = None
    reviews_count: Optional[int] = None
    price_range: Optional[str] = None

class VendorCreate(VendorBase):
    pass

class Vendor(VendorBase):
    id: int
    created_at: datetime
    updated_at: datetime
    services: List["Service"] = []

    class Config:
        from_attributes = True

class ServiceBase(BaseModel):
    service_type: str
    category_details: dict

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int
    vendor_id: int

    class Config:
        from_attributes = True
