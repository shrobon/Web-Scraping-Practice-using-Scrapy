# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from Hackernews.items import HackernewItem


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = (
        'https://www.news.ycombinator.com/',
    )

    def parse(self, response):
        titles = Selector(response).xpath('//tr[@class="athing"]/td[3]')

        for title in titles:
        	item = HackernewItem()
        	item['title'] = title.xpath("a[@href]/text()").extract()
        	item['url']   = title.xpath("a/@href").extract()
        	yield item