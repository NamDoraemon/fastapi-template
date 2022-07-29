#!/usr/bin/env python
# -*- coding: utf-8 -*-


def paginate_format(pagination):
    pagination.__dict__["pages"] = int(pagination.total / pagination.per_page) + (
        1 if pagination.total % pagination.per_page > 0 else 0
    )
    pagination.__dict__["has_previous"] = True if pagination.page > 1 else False
    pagination.__dict__["has_next"] = (
        True if pagination.page < pagination.pages else False
    )
    pagination.__dict__["next_page"] = (
        pagination.page + 1 if pagination.has_next is True else None
    )
    pagination.__dict__["previous_page"] = (
        pagination.page - 1 if pagination.has_previous is True else None
    )
    return pagination
