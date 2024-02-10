import scrapy
from pathlib import Path
from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # def start_requests(self):
    #     urls = [
    #         "https://quotes.toscrape.com/page/2/",
    #         "https://quotes.toscrape.com/page/3/",
    #         "https://quotes.toscrape.com/page/4/"
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    start_urls = [
        "https://quotes.toscrape.com/page/2/",
        "https://quotes.toscrape.com/page/3/",
        "https://quotes.toscrape.com/page/4/"
    ]

    custom_settings = {
        'FEEDS': {'data/data.json': {'format': 'json', 'overwrite': True}}
    }

    def parse(self, response):
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            tutorial_item = TutorialItem(
                text=text, author=author, tags=tags
            )
            yield tutorial_item
