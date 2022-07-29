#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlalchemy_utils as sa_utils
import arrow
import datetime
import enum


class BaseMixin:

    def to_dict(self):
        """
        Return an entity as dict
        :returns dict:
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def to_json(self):
        """
        Convert the entity to JSON
        :returns str:
        """
        data = {}
        for k, v in self.to_dict().items():
            if isinstance(
                    v, (datetime.datetime, sa_utils.ArrowType, arrow.Arrow)):
                v = v.isoformat()
            if isinstance(v, enum.Enum):
                v = v.value
            data[k] = v
        return data
