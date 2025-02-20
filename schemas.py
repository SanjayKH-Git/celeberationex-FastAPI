from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class VendorCategoryBase(BaseModel):
    name: str

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
