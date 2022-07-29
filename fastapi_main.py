#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uvicorn

from dotenv import load_dotenv

load_dotenv(override=False)  # noqa

from app.configs import config


def main():
    uvicorn.run(
        app="api.server:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True if config.ENV != "production" else False,
        workers=1,
    )


if __name__ == "__main__":
    main()
