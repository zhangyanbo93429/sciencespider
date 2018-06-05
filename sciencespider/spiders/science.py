# -*- coding: utf-8 -*-
import scrapy
from sciencespider.items import SciencespiderItem
from scrapy import Selector

class ScienceSpider(scrapy.Spider):
    name = 'science'
    allowed_domains = ['']
    start_urls = ['https://www.scientificamerican.com/']

    def parse(self, response):
        item = SciencespiderItem()
        selector = Selector(response)
        sites_list = response.xpath('//*[@id="latest-news"]/article[@class = "listing listing--with-thumb"]')

        #sites_list = selector.xpath('//article[@class = "listing listing--with-thumb"]').extract()
        for quote in sites_list:


            item['author'] = quote.xpath('p[@class = "t_meta listing__meta"]/text()').extract()[0]
            item['title'] = quote.xpath('h2/a/text()').extract()[0]
            item['link'] = quote.xpath('h2/a/@href').extract()[0]
            print('parsing')
            yield item


