from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user
from fastapi.staticfiles import StaticFiles
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(engine)



app= FastAPI()

app.include_router(user.router)
app.include_router(authentication.router)

@app.get('/')
def root():
    return 'Hello World'

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

