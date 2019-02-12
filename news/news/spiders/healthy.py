# -*- coding: utf-8 -*-
import scrapy


class HealthySpider(scrapy.Spider):
    name = 'healthy'
    allowed_domains = ['health.sohu.com']
    start_urls = ['http://health.sohu.com']

    def parse(self, response):
        html = response.text
        a = response.xpath('//a/@href').extract()
        print(a)
        # print(html)
        pass
