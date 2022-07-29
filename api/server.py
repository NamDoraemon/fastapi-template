#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.exceptions import CustomException
from .router import router
from app.helpers.cache import Cache
from app.helpers.cache.custom_key_maker import CustomKeyMaker
from app.helpers.cache.redis_backend import RedisBackend
from app.middlewares import SQLAlchemyMiddleware
from app.configs import config


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(router)


def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(status_code=exc.code,
                            content={
                                "error_code": exc.error_code,
                                "message": exc.message
                            })


def init_middleware(app: FastAPI) -> None:
    app.add_middleware(SQLAlchemyMiddleware)


def init_cache() -> None:
    Cache.init(backend=RedisBackend(), key_maker=CustomKeyMaker())


def create_app() -> FastAPI:
    app = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        # dependencies=[Depends(Logging)],
    )
    init_routers(app=app)
    init_cors(app=app)
    init_listeners(app=app)
    init_middleware(app=app)
    init_cache()
    return app


app = create_app()
