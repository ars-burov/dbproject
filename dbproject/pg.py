from configargparse import Namespace
from aiohttp.web_app import Application
from asyncpgsa import PG

async def setup_pg(app: Application, args: Namespace) -> PG:
    app['pg'] = PG()
    await app['pg'].init(
        'postgres://user:password@localhost/dbproject',
    )
    await app['pg'].fetchval('SELECT 1')

    try:
        yield
    finally:
        await app['pg'].pool.close()
