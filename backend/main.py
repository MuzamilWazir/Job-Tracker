from fastapi import FastAPI

from database import base , engine ,test_connection



base.metadata.create_all(engine)
test_connection()

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}