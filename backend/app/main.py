from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, models, schemas
from datetime import date, datetime, timezone

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    database.init_db()

@app.post("/subscribe")
def subscribe(sub: schemas.SubscribeRequest, db: Session = Depends(get_db)):
    # Check if email already exists
    existing = db.query(models.Subscriber).filter(models.Subscriber.email == sub.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already subscribed")

    now = datetime.now(timezone.utc)
    today = date.today()
    subscriber = models.Subscriber(
        email=sub.email,
        project=sub.project,
        country=sub.country,
        city=sub.city,
        state=sub.state,
        location=sub.location,
        subscribe_time=now,
        subscribe_date=today
    )
    db.add(subscriber)
    db.commit()
    db.refresh(subscriber)
    return {"message": "Subscribed successfully!"}

@app.get("/ping")
def read_root():
    return {"Hello": "World"}