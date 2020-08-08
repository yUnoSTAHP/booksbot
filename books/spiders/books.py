# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):
            yield {
                'email': quote.xpath('//a[@data-analytics='link.contact.email']').get()
            }

        next_page = response.css('ul.paginator li.pageend a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
