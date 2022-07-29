#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

product_supplier_router = APIRouter()

@product_supplier_router.post("", tags=["Product Supplier"])
async def post():
    # TODO: Viết API
    return { "success": True }


@product_supplier_router.put("", tags=["Product Supplier"])
async def put():
    # TODO: Viết API
    return { "success": True }

@product_supplier_router.get("by-supplier", tags=["Product Supplier"])
async def get_by_product_supplier():
    # TODO: Viết API
    return { "success": True }

@product_supplier_router.get("by-productid", tags=["Product Supplier"])
async def get_by_product_id():
    # TODO: Viết API
    return { "success": True }

@product_supplier_router.get("<int:id>", tags=["Product Supplier"])
async def update_by_id():
    # TODO: Viết API
    return { "success": True }
