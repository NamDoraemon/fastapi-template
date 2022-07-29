#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

product_parent_router = APIRouter()


@product_parent_router.get("", tags=["Product Parent"])
async def get():
    # TODO: Viết API
    return {
        "success": True,
        "data": {},
    }

@product_parent_router.get("<int:id>", tags=["Product Parent"])
async def get_by_id(id):
    # TODO: Viết API
    return {
        "success": True,
        "data": {}
    }

@product_parent_router.put("<int:id>", tags=["Product Parent"])
async def update_by_id(id):
    # TODO: Viết API
    return {
        "success": True,
        "data": {}
    }