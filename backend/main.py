from fastapi import FastAPI
from database import base , engine ,test_connection
from routers.company import router
from routers.auth import router as auth_router



base.metadata.create_all(engine)
test_connection()

app = FastAPI()

app.include_router(router, prefix="/company", tags=["Company"])
app.include_router(auth_router, tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Hello World!"}