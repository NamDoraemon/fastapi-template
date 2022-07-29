#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import or_, select
from typing import List

from app.db import session, Transactional
from app.helpers.utils import paginate_format
from app.models import Product


class ProductRepository:

    def __init__(self):
        self.model = Product

    async def get_by_id(self, id) -> Product:
        query = select(self.model).where(Product.id == id)
        result = await session.execute(query)
        return result.scalars().first()

    async def is_exists_code(self, codex: str) -> bool:
        query = select(self.model).where(Product.codex == codex)
        result = await session.execute(query)
        product = result.scalars().first()
        if product:
            return True
        return False

    @Transactional()
    async def create(self, **kwargs) -> Product:
        product = self.model(**kwargs)
        session.add(product)
        return product

    @Transactional()
    async def update(self, id, **kwargs) -> Product:
        product = await self.get_by_id(id)
        for key in kwargs:
            if key == "quantity_stock_added" and kwargs.get(
                    "quantity_stock_added") is not None:
                setattr(
                    product,
                    "code_stock",
                    product.code_stock + kwargs.get("quantity_stock_added"),
                )
            elif key != "id" and kwargs.get(key) is not None:
                setattr(product, key, kwargs.get(key))
        return product

    async def get_by_code(self, codex: str) -> List[Product]:
        query = select(self.model).where(Product.codex == codex)
        result = await session.execute(query)
        products = result.scalars().all()
        return products

    async def get_with_pagination(self, **kwargs):
        page = kwargs.get("page") or 1
        per_page = kwargs.get("per_page") or 20
        query = select(self.model)
        for key in kwargs:
            if hasattr(self.model, key) and kwargs.get(key) is not None:
                query = query.where(getattr(self.model, key) == kwargs.get(key))
            elif key == 'title_suggest':
                if kwargs.get(key) is not None and kwargs.get(key) != "":
                    query = query.where(self.model.title.like(f"%{kwargs.get(key)}%"))
            elif key == "codex_suggest":
                if kwargs.get(key) is not None and kwargs.get(key) != "":
                    query = query.where(or_(
                        self.model.codex.like(f"%{kwargs.get(key)}%"),
                        self.model.id == kwargs.get(key),
                    ))
            elif key == "ids":
                if kwargs.get(key) is not None and len(kwargs.get(key)) > 0:
                    query = query.where(self.model.id.in_(kwargs.get(key)))
        products = query.order_by(desc(self.model.id)).paginate(page=page, per_page=per_page)
        if products is None:
            return products

        products = paginate_format(products)
        print(products)
        return products

product_repo = ProductRepository()
