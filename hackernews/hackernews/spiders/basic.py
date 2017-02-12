# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = (
        'http://www.news.ycombinator.com/',
    )

    def parse(self, response):
        pass
