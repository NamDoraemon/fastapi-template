#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from .ping import ping_router
from .product import product_router

sub_router = APIRouter()
sub_router.include_router(ping_router, prefix="/ping", tags=["Ping"])
sub_router.include_router(product_router, prefix="/product", tags=["Product"])

__all__ = ["sub_router"]
