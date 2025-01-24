from fastapi import FastAPI
from routes.logisticsRoute import logisticsRoute

app = FastAPI()

app.include_router(logisticsRoute)