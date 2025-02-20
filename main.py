from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/vendors/", response_model=schemas.Vendor)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    db_vendor = models.Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

@app.get("/vendors/{vendor_id}", response_model=schemas.Vendor)
def read_vendor(vendor_id: int, db: Session = Depends(get_db)):
    db_vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if db_vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return db_vendor

@app.post("/vendors/{vendor_id}/services/", response_model=schemas.Service)
def create_service(vendor_id: int, service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    db_vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if db_vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    db_service = models.Service(**service.dict(), vendor_id=vendor_id)
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

@app.get("/vendors/{vendor_id}/services/", response_model=List[schemas.Service])
def read_services(vendor_id: int, db: Session = Depends(get_db)):
    db_services = db.query(models.Service).filter(models.Service.vendor_id == vendor_id).all()
    return db_services
