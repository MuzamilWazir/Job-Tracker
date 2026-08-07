from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

try:
    from .config import settings
except ImportError:  # pragma: no cover - allows running as a top-level module
    from config import settings

base = declarative_base()

engine = create_engine(url=settings.DATABASE_URL, echo=True)

local_session = sessionmaker(bind=engine)


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()