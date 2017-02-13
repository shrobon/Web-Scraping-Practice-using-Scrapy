# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from socrata.items import SocrataItem

class OpendataSpider(CrawlSpider):
    name = "opencrawl"
    allowed_domains = ["opendata.socrata.com"]
    start_urls = ['http://opendata.socrata.com/']
    rules = [
    Rule(LinkExtractor(allow='browse\?&page=\d*'),
    	callback='parse_item',follow=True)
    ]

    def parse(self, response):
        titles = scrapy.Selector(response).xpath("//div[@itemtype='http://schema.org/Dataset']")
        
        for title in titles:
        	item = SocrataItem()
        	item['text'] =title.xpath("//a/span[@itemprop='name']/text()").extract()
        	item['url']  =title.xpath("//a[@href=contains('','https://opendata.socrata.com')]").extract()
        	item['views']=title.xpath("//div[contains(@class,'view-count-value')]/text()").extract()
        	yield item
