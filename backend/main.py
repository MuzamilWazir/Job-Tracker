from fastapi import FastAPI
from database import base, engine, test_connection
from routers.company import router as company_router
from routers.auth import router as auth_router


app = FastAPI()

app.include_router(company_router, tags=["Company"])
app.include_router(auth_router, tags=["Authentication"])


@app.on_event("startup")
def init_db() -> None:
    base.metadata.create_all(engine)
    test_connection()


@app.get("/")
def read_root() -> dict:
    return {"message": "Hello World!"}
