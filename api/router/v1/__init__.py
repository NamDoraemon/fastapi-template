#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from .ping import ping_router
from .product import product_router
from .product_parent import product_parent_router
from .product_supplier import product_supplier_router

v1_router = APIRouter()

v1_router.include_router(ping_router, prefix="/ping")
v1_router.include_router(product_router, prefix="/product")
v1_router.include_router(product_parent_router, prefix="/product_parent")
v1_router.include_router(product_supplier_router, prefix="/product_supplier")
