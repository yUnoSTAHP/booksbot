# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "local nagelstudio"
    allowed_domains = ["tel.local.ch"]
    start_urls = [
        'https://tel.local.ch/de/q/schweiz/nagelstudio',
    ]

    def parse(self, response):
        for x in response.xpath('//a[@data-kpi-type="email"]/span[@class="visible-print"]').getall():
            yield {"mail": x}
       
	   //a[@class='pagination-link' and @rel="next"]
        next_page = response.css('a.pagination-link[rel="next"]::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
