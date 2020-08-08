# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "coiffeurvergleich"
    allowed_domains = ["www.coiffeurvergleich.ch"]
    start_urls = [
        'https://www.coiffeurvergleich.ch/coiffeur.php?p=10&geschlecht=0',
    ]

    def parse(self, response):
        response.xpath('//a[@data-analytics="link.contact.email"]').getall()

        next_page = response.css('ul.paginator li.pageend a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
