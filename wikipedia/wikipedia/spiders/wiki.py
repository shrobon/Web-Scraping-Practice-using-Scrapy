# -*- coding: utf-8 -*-
import scrapy
from wikipedia.items import WikipediaItem

class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ['https://en.wikipedia.org/wiki/Category:2014_films']

    def parse(self, response):
        titles = scrapy.Selector(response).xpath('//div[@id="mw-pages"]//li') #bypassing child elements // 
        for title in titles:
        	item = WikipediaItem()
        	url = title.select("a/@href").extract()
        	item['title'] = title.select("a/text()").extract()
        	item['url']   = url[0]
        	yield item
