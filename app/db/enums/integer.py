#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.types import Integer

from app.db.enums import BaseEnum


class IntegerEnum(BaseEnum):
    impl = Integer
