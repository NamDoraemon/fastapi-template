#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.types import String

from app.db.enums import BaseEnum


class StringEnum(BaseEnum):
    impl = String
