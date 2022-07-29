#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.schemas import PingResponseSchema

ping_router = APIRouter()


@ping_router.get("", response_model=PingResponseSchema, tags=["Ping"])
async def ping():
    return {"status": 2, "message": "pong"}
