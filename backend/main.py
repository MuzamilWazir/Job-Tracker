from fastapi import FastAPI

try:
    from .database import base, engine
except ImportError:  # pragma: no cover - allows running as a top-level module
    from database import base, engine

base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}