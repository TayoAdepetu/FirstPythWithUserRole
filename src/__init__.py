from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting...")
    await init_db()
    yield
    print(f"Server has been stopped.")


version = "v1"

app = FastAPI(
    title="BizCertify API",
    description="AI API For BizCertify",
    version=version,
    # lifespan=life_span, #commented out since we are now using alembic to do db migration, so that our init db will not run again
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
app.include_router(review_router, prefix=f"/api/{version}/reviews", tags=["reviews"])
