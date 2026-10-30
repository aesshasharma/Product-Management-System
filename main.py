from fastapi import FastAPI
from route.productroute import router

app = FastAPI(title="Product Management API")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Product Management API"}


