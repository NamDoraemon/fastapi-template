#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.services import ServiceProduct

product_router = APIRouter()


@product_router.get("/")
async def get():
    products = ServiceProduct.get()
    return products
    # ServiceProduct.get(**kwargs)
    # response_data = {
    #     "success": True,
    #     "data": {
    #         "items": products.items,
    #         "has_next": products.has_next,
    #         "has_previous": products.has_previous,
    #         "next_page": products.next_page,
    #         "previous_page": products.previous_page,
    #         "page": products.page,
    #         "pages": products.pages,
    #         "per_page": products.per_page,
    #         "total": products.total
    #     }
    # }
    # return response_data
