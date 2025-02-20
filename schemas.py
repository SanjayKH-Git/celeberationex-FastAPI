from pydantic import BaseModel
from typing import Optional, Dict, Any

class VendorCategoryBase(BaseModel):
    name: str
    details: Optional[Dict[str, Any]] = None  
    image_url: Optional[str] = None

class VendorCategoryCreate(VendorCategoryBase):
    pass

class VendorCategory(VendorCategoryBase):
    id: int

    class Config:
        orm_mode = True

class CeleberationListBase(BaseModel):
    celeberation_name: str

class CeleberationListCreate(CeleberationListBase):
    pass

class CeleberationList(CeleberationListBase):
    id: int

    class Config:
        orm_mode = True
