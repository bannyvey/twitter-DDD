import asyncio
from contextlib import asynccontextmanager

import uvicorn
from alembic import command
from alembic.config import Config
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware

from my_twitter.core.error.base_exception import BaseError
from .features import router



async def run_migrations():
    alembic_cfg = Config("alembic.ini")
    await asyncio.to_thread(command.upgrade, alembic_cfg, "head")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await run_migrations()
    yield


app = FastAPI(lifespan=lifespan)  # lifespan=lifespan

app.include_router(router)


@app.get('/')
async def root():
    return {"message": "Hello World"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "result": False,
            "error_type": "ValidationError",
            "error_message": str(exc)
        }
    )


@app.exception_handler(Exception)
async def universal_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "result": False,
            "error_type": exc.__class__.__name__,
            "error_message": str(exc)
        }
    )


@app.exception_handler(BaseError)
async def base_error_handler(request, exc: BaseError):
    return JSONResponse(
        status_code=400,
        content={
            "result": False,
            "error_type": exc.__class__.__name__,
            "error_message": exc.message
        }
    )


if __name__ == "__main__":
    uvicorn.run("my_twitter.main:app", host="127.0.0.1", port=8000, reload=True)
