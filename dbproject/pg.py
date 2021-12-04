from configargparse import Namespace
from aiohttp.web_app import Application
from asyncpgsa import PG
from config import config

params_db = config('postgresql')

con_string = 'postgres://' + params_db['user'] + ':' \
+ params_db['password'] + '@' + params_db['host'] + '/' + params_db['database']

async def setup_pg(app: Application, args: Namespace) -> PG:
    app['pg'] = PG()
    await app['pg'].init(
        con_string,
    )
    
    try:
        yield
    finally:
        await app['pg'].pool.close()
