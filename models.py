from sqlalchemy import Column, Integer, String, JSON
from database import Base

class VendorCategory(Base):
    __tablename__ = "vendor_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    details = Column(JSON)  # JSON type for details
    image_url = Column(String)  # Add this line

class CeleberationList(Base):
    __tablename__ = "celeberation_list"
    id = Column(Integer, primary_key=True, index=True)
    celeberation_name = Column(String, index=True)
