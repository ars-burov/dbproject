from functools import partial

from aiohttp.web_app import Application
from configargparse import Namespace
from aiohttp import PAYLOAD_REGISTRY

from dbproject.api.handlers import HANDLERS
from dbproject.pg import setup_pg


def create_app(args: Namespace) -> Application:
    app = Application()

    app.cleanup_ctx.append(partial(setup_pg, args=args))

    for handler in HANDLERS:
        app.router.add_route('*', handler.URL_PATH, handler)

    return app