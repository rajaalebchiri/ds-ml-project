#!/usr/bin/env python
# asynchronous programming using AIOHTTP
import aiohttp
import asyncio
from aiohttp import web

# example Client
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://news.ycombinator.com/') as response:
            print('Status:', response.status)
            print('Content-Type:', response.headers['content-type'])
            html = await response.text()
            print("Body:", html[:15], "...")

# asyncio.run(main())

# example Server
async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)