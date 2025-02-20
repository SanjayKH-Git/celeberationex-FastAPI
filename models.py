from sqlalchemy import Column, Integer, String, DECIMAL, JSON, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    category = Column(String, nullable=False)
    location_city = Column(String)
    location_state = Column(String)
    contact_number = Column(String)
    email = Column(String)
    website = Column(String)
    rating = Column(DECIMAL(3, 2))
    reviews_count = Column(Integer)
    price_range = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    services = relationship("Service", back_populates="vendor")

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    service_type = Column(String, nullable=False)
    category_details = Column(JSON, nullable=False)
    vendor = relationship("Vendor", back_populates="services")
