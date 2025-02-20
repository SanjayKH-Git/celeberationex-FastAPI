from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, database
from typing import List
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"location": "celeberationex root"}

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/vendor_categories/", response_model=schemas.VendorCategory)
def create_or_update_vendor_category(vendor_category: schemas.VendorCategoryCreate, db: Session = Depends(get_db)):
    try:
        db_vendor_category = db.query(models.VendorCategory).filter(models.VendorCategory.name == vendor_category.name).first()
        if db_vendor_category:
            for key, value in vendor_category.dict().items():
                setattr(db_vendor_category, key, value)
            db.commit()
            db.refresh(db_vendor_category)
        else:
            db_vendor_category = models.VendorCategory(**vendor_category.dict())
            db.add(db_vendor_category)
            db.commit()
            db.refresh(db_vendor_category)
        return db_vendor_category
    except Exception as e:
        logger.error(f"Error creating or updating vendor category: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@app.get("/vendor_categories/{name}", response_model=schemas.VendorCategory)
def read_vendor_category(name: str, db: Session = Depends(get_db)):
    try:
        db_vendor_category = db.query(models.VendorCategory).filter(models.VendorCategory.name == name).first()
        if db_vendor_category is None:
            raise HTTPException(status_code=404, detail="Vendor category not found")
        return db_vendor_category
    except Exception as e:
        logger.error(f"Error reading vendor category: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@app.get("/vendor_categories_config", response_model=List[str])
def get_vendor_categories_config(db: Session = Depends(get_db)):
    try:
        categories = db.query(models.VendorCategory).all()
        return [category.name for category in categories]
    except Exception as e:
        logger.error(f"Error getting vendor categories config: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@app.post("/celeberation_list/", response_model=List[str])
def create_celeberation(celeberations: List[schemas.CeleberationListCreate], db: Session = Depends(get_db)):
    try:
        # Delete all existing records
        db.query(models.CeleberationList).delete()

        # Insert new records
        db_celeberations = [models.CeleberationList(**celeberation.dict()) for celeberation in celeberations]
        db.add_all(db_celeberations)
        db.commit()

        # Refresh all new records
        for db_celeberation in db_celeberations:
            db.refresh(db_celeberation)

        return [celeberation.celeberation_name for celeberation in db_celeberations]
    except Exception as e:
        logger.error(f"Error creating celebration list: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@app.get("/celeberation_list/", response_model=List[str])
def read_celeberation_list(db: Session = Depends(get_db)):
    try:
        return [celeberation.celeberation_name for celeberation in db.query(models.CeleberationList).all()]
    except Exception as e:
        logger.error(f"Error reading celebration list: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
