from aiohttp.web_response import Response
from aiohttp_apispec import docs

from .base import BaseView

class HelloView(BaseView):
    URL_PATH = ''

    @docs(summary='Hello world')
    async def get(self):
        pg_resp = await self.pg.fetch('SELECT 1')
        return Response(body=f'{pg_resp} Hello world')
