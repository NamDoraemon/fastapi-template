#!/usr/bin/env python
# -*- coding: utf-8 -*-
import aioredis

from app.configs import config

redis = aioredis.from_url(
    url=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}")
