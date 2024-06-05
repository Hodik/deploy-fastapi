from fastapi import FastAPI
from mangum import Mangum
from config import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if not settings.ENVIRONMENT == "local":
    app = Mangum(app)
