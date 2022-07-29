#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field
from app.enums import UrBoxStatusEnum, ProductTypeEnum
from typing import Union


class ProductSchema(BaseModel):
    id: int
    product_parent_id: int
    codex: str
    title: str
    image: Union[str, None]
    type: ProductTypeEnum
    unit: Union[str, None]
    code_min: int
    code_stock: int
    valuex: int
    status: int
    created: str
    updated: str

    class Config:
        schema_extra = {
            "example": {
                "id": 10113,
                "product_parent_id": 1,
                "codex": "UrBox016",
                "title": "Test Product 016",
                "image": None,
                "type": 1,
                "unit": "VNĐ",
                "code_min": 0,
                "code_stock": 0,
                "valuex": 10000,
                "status": 2,
                "created": "2022-06-16T14:16:31",
                "updated": "2022-06-16T14:16:31"
            }
        }


class GetProductListRequestSchema(BaseModel):
    ids: str = Field(None, description="ids")
    title_suggest: str = Field(None, description="title_suggest")
    codex_suggest: str = Field(None, description="codex_suggest")
    codex: str = Field(None, description="codex")
    title: str = Field(None, description="title")
    image: str = Field(None, description="image")
    quantity: int = Field(None, description="quantity")
    type: ProductTypeEnum = Field(None, description="type")
    unit: str = Field(None, description="unit")
    status: UrBoxStatusEnum = Field(None, description="status")
    page: int = Field(1, title='page', description="page", gt=0)


class ProductUpdateRequestSchema(BaseModel):
    id: int = Field(..., description="product id", gt=0)
    codex: str = Field(None, description="product codex")
    title: str = Field(None, description="product title")
    image: str = Field(None, description="product image")
    quantity: int = Field(None, description="product quantity")
    quantity_stock_added: int = Field(
        None, description="product quantity stock added")
    type: ProductTypeEnum = Field(None, description="product type")
    unit: str = Field(None, description="product unit")
    status: UrBoxStatusEnum = Field(None, description="product status")
    code_min: int = Field(0, description="product code min")
    valuex: int = Field(None, description="product valuex")

    class Config:
        schema_extra = {
            "example": {
                "id": 10113,
                "code_min": 10,
            }
        }


class ProductCreateRequestSchema(BaseModel):
    codex: str = Field(..., description="product codex")
    title: str = Field(..., description="product title")
    image: str = Field(None, description="product image")
    code_min: int = Field(0, description="product code min", gte=0)
    code_stock: int = Field(0, description="product code stock", gte=0)
    type: ProductTypeEnum = Field(..., description="product type")
    unit: str = Field(..., description="product unit")
    status: UrBoxStatusEnum = Field(UrBoxStatusEnum.Activate,
                                    description="product status")
    valuex: int = Field(..., description="product valuex", gte=0)
    product_parent_id: int = Field(..., description="product parent id", gt=0)

    class Config:
        schema_extra = {
            "example": {
                "codex": "UrBox001",
                "title": "Test Product 001",
                "code_min": 0,
                "code_stock": 0,
                "type": 1,
                "unit": "VNĐ",
                "status": 2,
                "valuex": 10000,
                "product_parent_id": 1,
            }
        }


class ProductCreateResponseSchema(BaseModel):
    success: bool
    data: ProductSchema

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "data": {
                    "id": 10113,
                    "product_parent_id": 1,
                    "codex": "UrBox016",
                    "title": "Test Product 016",
                    "image": None,
                    "type": 1,
                    "unit": "VNĐ",
                    "code_min": 0,
                    "code_stock": 0,
                    "valuex": 10000,
                    "status": 2,
                    "created": "2022-06-16T14:16:31",
                    "updated": "2022-06-16T14:16:31"
                }
            }
        }
