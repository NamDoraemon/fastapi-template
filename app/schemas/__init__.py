#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field

from .product import *
from .ping import *


class ExceptionResponseSchema(BaseModel):
    error: str
