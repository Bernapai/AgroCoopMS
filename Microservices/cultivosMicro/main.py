from fastapi import FastAPI
from routes.cultivosRoute import cultivoRoute

app = FastAPI()

app.include_router(cultivoRoute)