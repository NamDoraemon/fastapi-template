#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter
import psutil

ping_router = APIRouter()


@ping_router.get("/")
async def pong():
    return {
        "status": 2,
        "message": "pong",
        "data": {
            "CPU": psutil.cpu_percent(),
            "RAM": psutil.virtual_memory().percent
        }
    }
