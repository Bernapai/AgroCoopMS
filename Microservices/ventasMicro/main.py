from fastapi import FastAPI
from routes.ventasRoute import ventasRoute

app = FastAPI()

app.include_router(ventasRoute)