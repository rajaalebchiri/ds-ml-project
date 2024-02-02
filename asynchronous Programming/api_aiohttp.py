#!/usr/bin/env python
""" simple RESTful API using aiohttp: """
from aiohttp import web
import json
import asyncio
import aiohttp
from scrapy import Selector


def parse_html(html):
    selector = Selector(text=html)
    # Extract titles using XPath
    titles = selector.css("td.title span a::text").getall()
    print(titles)
    return titles


async def handle(request):
    response_obj = {
        "status": "success",
        "Features": {
            "Get ycombinator news": "/hackernews/posts",
        },
    }
    return web.Response(text=json.dumps(response_obj, indent=4))


async def get_news(request):
    try:
        print("Collecting news ...")
        async with aiohttp.ClientSession() as session:
            async with session.get("https://news.ycombinator.com/") as response:
                print("Status:", response.status)
                print("Content-Type:", response.headers["content-type"])
                html = await response.text()
        response_obj = {"results": parse_html(html=html)}
        return web.Response(text=json.dumps(response_obj, indent=4), status=500)
    except Exception as e:
        response_obj = {"status": "failed", "reason": str(e)}
        return web.Response(text=json.dumps(response_obj, indent=4), status=500)


app = web.Application()
app.router.add_get("/", handle)
app.router.add_get("/hackernews/posts", get_news)

web.run_app(app)
