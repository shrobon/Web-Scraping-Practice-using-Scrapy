# -*- coding: utf-8 -*-
import scrapy
from socrata.items import SocrataItem

class OpendataSpider(scrapy.Spider):
    name = "opendata"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = ['http://opendata.socrata.com/']

    def parse(self, response):
        titles = scrapy.Selector(response).xpath("//div[@itemtype='http://schema.org/Dataset']")
        for title in titles:
        	item = SocrataItem()
        	item['text'] =title.select("//a/span[@itemprop='name']/text()").extract()
        	item['url']  =title.select("//a/@href").extract()[0]
        	item['views']=title.select("//div[contains(@class,'view-count-value')]/text()").extract()[0].replace('\n',"").replace(" ","")
        	yield item
