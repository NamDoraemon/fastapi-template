#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from app.db.enums import IntegerEnum
from app.db.mixins import TimestampUrBoxMixin
from app.db.mixins.base import BaseMixin
from app.enums.product import ProductTypeEnum
from app.enums.status import UrBoxStatusEnum
from app.db import Base


class Product(Base, BaseMixin, TimestampUrBoxMixin):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    product_parent_id = Column(Integer,
                               index=False,
                               unique=False,
                               nullable=False)
    codex = Column(String(70), index=False, unique=False, nullable=True)
    title = Column(String(255), index=False, unique=False, nullable=True)
    image = Column(String(255), index=False, unique=False, nullable=True)
    type = Column("type",
                  IntegerEnum(ProductTypeEnum),
                  index=False,
                  unique=False,
                  nullable=True)
    unit = Column(String(50), index=False, unique=False, nullable=True)
    code_min = Column(Integer, index=False, unique=False, nullable=True)
    code_stock = Column(Integer, index=False, unique=False, nullable=True)
    valuex = Column(Integer, index=False, unique=False, nullable=True)
    status = Column("status",
                    IntegerEnum(UrBoxStatusEnum),
                    index=False,
                    unique=False,
                    nullable=True)

    def __init__(self, **kwargs):
        self.codex = kwargs.get("codex") or None
        self.title = kwargs.get("title") or None
        self.image = kwargs.get("image") or None
        self.type = kwargs.get("type") or ProductTypeEnum.Single
        self.unit = kwargs.get("unit") or 0
        self.status = kwargs.get("status") or UrBoxStatusEnum.Activate
        self.code_min = kwargs.get("code_min") or 0
        self.code_stock = kwargs.get("code_stock") or 0
        self.valuex = kwargs.get("valuex") or 0
        self.product_parent_id = kwargs.get("product_parent_id") or 0
