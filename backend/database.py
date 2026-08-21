from sqlalchemy import create_engine , text
from sqlalchemy.orm import declarative_base, sessionmaker

try:
    from .config import settings
except ImportError:  # pragma: no cover - allows running as a top-level module
    from config import settings

base = declarative_base()

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=True,
    connect_args={"sslmode": "require"},
    pool_pre_ping=True,
    pool_recycle=300
)

SessionLocal = sessionmaker(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Successfully connected to Neon Database")
    except Exception as e:
        print("❌ Failed to connect to the database")
        print(e)