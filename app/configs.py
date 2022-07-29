#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib

from pydantic import BaseSettings


class ConfigMysql(object):
    SQLALCHEMY_ECHO = False
    DB_USERNAME = os.environ.get("DB_MYSQL_USER") or ""
    DB_PASSWORD = os.environ.get("DB_MYSQL_PASS") or ""
    DB_HOST = os.environ.get("DB_MYSQL_HOST")
    DB_PORT = os.environ.get("DB_MYSQL_PORT")
    DB_NAME = os.environ.get("DB_MYSQL_DBNAME")
    DATABASE_URL = f"mysql+aiomysql://{urllib.parse.quote(DB_USERNAME)}:{urllib.parse.quote(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    WRITER_DB_URL = DATABASE_URL
    READER_DB_URL = DATABASE_URL
    print(DATABASE_URL)


class Config(BaseSettings, ConfigMysql):
    ENV: str = os.environ.get("ENV")
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    SENTRY_SDN: str = None
    REDIS_HOST: str = os.environ.get("REDIS_HOST") or "localhost"
    REDIS_PORT: int = (os.environ.get("REDIS_PORT")
                       and int(os.environ.get("REDIS_PORT"))) or 6379
    REDIS_DB: int = (os.environ.get("REDIS_DB")
                     and int(os.environ.get("REDIS_DB"))) or 6


class DevelopmentConfig(Config):
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    ...


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = os.environ.get("ENV") or "local"
    config_type = {
        "development": DevelopmentConfig(),
        "local": LocalConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
