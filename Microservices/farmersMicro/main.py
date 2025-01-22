from fastapi import FastAPI
from routes.sociosRoute import socioRoute

app = FastAPI()


app.include_router(socioRoute)