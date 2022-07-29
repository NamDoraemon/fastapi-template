# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app.exceptions.base import DuplicateValueException, NotFoundException, BadRequestException
from app.models import Product
from app.repositories import product_repo


class ProductService:

    def __init__(self):
        pass

    async def create(self, **kwargs) -> Product:
        is_exists = await product_repo.is_exists_code(kwargs.get("codex"))
        if is_exists:
            raise DuplicateValueException(
                message="The production code is exists")

        product = await product_repo.create(**kwargs)
        if product is None or product.id is None:
            return None

        return product

    async def update(self, id: int, **kwargs) -> Product:
        product = await product_repo.get_by_id(id)

        if not product:
            raise NotFoundException()

        if kwargs.get("codex"):
            products_duplicated = product_repo.get_by_code(kwargs.get("codex"))
            product_ids_duplicated = [
                product.id for product in products_duplicated
            ]

            if len(products_duplicated
                   ) > 0 and product.id not in product_ids_duplicated:
                raise DuplicateValueException(
                    message="The production code is exists")
            elif product.id in product_ids_duplicated and len(
                    products_duplicated) > 1:
                raise DuplicateValueException(
                    message="The production code is exists")

        product = await product_repo.update(id, **kwargs)

        # product_suppliers = product_supplier_repo.get_product_suppliers_by_product_id(
        #     args.get("id")
        # )
        #
        # data = []
        # if len(product_suppliers) > 0:
        #     for product_supplier in product_suppliers:
        #         product_supplier_json = product_supplier.json
        #         data.append(product_supplier_json)

        return product

    async def get(self, **kwargs):
        ids = []

        if kwargs.get("ids") is not None:
            ids = kwargs.get("ids").split(",")
            if len(ids) > 100:
                raise BadRequestException(message="Input too large")

        products = product_repo.get_with_pagination(
            ids=ids,
            id=kwargs.get("id"),
            codex=kwargs.get("codex"),
            title=kwargs.get("title"),
            status=kwargs.get("status"),
            type=kwargs.get("type"),
            page=kwargs.get("page"),
            per_page=kwargs.get("per_page"),
            title_suggest=kwargs.get("title_suggest"),
            codex_suggest=kwargs.get("codex_suggest"),
        )

        if products is None:
            return products

        product_items = []
        if len(products.items) > 0:
            for item in products.items:
                product_items.append(item.to_json())

        products.__dict__["items"] = product_items
        return products


product_service = ProductService()
