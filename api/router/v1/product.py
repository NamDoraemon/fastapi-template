#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends

from app.schemas import GetProductListRequestSchema, ProductUpdateRequestSchema, ProductCreateRequestSchema, ProductCreateResponseSchema
from app.services import product_service

product_router = APIRouter()


@product_router.get("", tags=["Products"])
async def get(request: GetProductListRequestSchema = Depends()):
    request = request.dict(exclude_none=True)
    pagination = await product_service.get(**request)
    return {
        "success": True,
        # "data": {
        #     "items": pagination.items,
        #     "has_next": pagination.has_next,
        #     "has_previous": pagination.has_previous,
        #     "next_page": pagination.next_page,
        #     "previous_page": pagination.previous_page,
        #     "page": pagination.page,
        #     "pages": pagination.pages,
        #     "per_page": pagination.per_page,
        #     "total": pagination.total,
        # }
    }


@product_router.put("", tags=["Products"])
async def put(request: ProductUpdateRequestSchema):
    request = request.dict(exclude_none=True, exclude_unset=True)
    params = request.copy()
    del params["id"]

    product = await product_service.update(request.get('id'), **params)
    if product:
        return {"success": True, "data": product.to_json()}
    return {
        "success": False,
        "metadata": {
            "errors": [{
                "code": 500,
                "message": "Internal Server"
            }]
        },
    }


@product_router.post("",
                     response_model=ProductCreateResponseSchema,
                     tags=["Products"])
async def post(request: ProductCreateRequestSchema):
    request = request.dict(exclude_none=True, exclude_unset=True)
    product = await product_service.create(**request)

    if product:
        return {"success": True, "data": product.to_json()}
    return {
        "success": False,
        "metadata": {
            "errors": [{
                "code": 500,
                "message": "Internal Server"
            }]
        },
    }

@product_router.get("<int:id>/product-supplier", tags=["Products"])
async def get_product_supplier(id: int):
    # TODO: Viết API
    return {
        "success": True,
        "data": "",
    }

@product_router.post("<int:id>/generate-code", tags=["Products"])
async def generate_code(id: int):
    # TODO: Viết API
    return {
        "success": True,
        "data": "",
    }

@product_router.get("<int:id>", tags=["Products"])
async def get_detail(id: int):
    # TODO: Viết API
    return {
        "success": True,
        "data": "",
    }

@product_router.put("<int:id>", tags=["Products"])
async def update_by_id(id: int):
    # TODO: Viết API
    return {
        "success": True,
        "data": "",
    }
