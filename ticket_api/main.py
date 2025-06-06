from fastapi import FastAPI
from .routes import router
from .database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ticket API")
app.include_router(router)
