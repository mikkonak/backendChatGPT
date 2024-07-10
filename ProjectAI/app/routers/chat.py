from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, dependencies

router = APIRouter()

@router.post("/send/", response_model=schemas.Message)
def send_message(message: schemas.MessageCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_message(db=db, message=message)

@router.get("/messages/", response_model=List[schemas.Message])
def get_messages(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    return crud.get_messages(db, skip=skip, limit=limit)
