from sqlalchemy import Column, Integer, String
from database import Base

class VendorCategory(Base):
    __tablename__ = "vendor_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class CeleberationList(Base):
    __tablename__ = "celeberation_list"
    id = Column(Integer, primary_key=True, index=True)
    celeberation_name = Column(String, index=True)
