from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import database, models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Invoice",version=0.01)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def default():
    return {"message","Welcome to Invoice API"}