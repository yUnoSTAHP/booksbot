# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "coiffeurvergleich"
    allowed_domains = ["www.coiffeurvergleich.ch"]
    start_urls = [
'https://coiffeursearch.ch/index.php?L=0&type=999&tx_klinkcosumitglieder_ajax[controller]=Salon&tx_klinkcosumitglieder_ajax[action]=detailjson&tx_klinkcosumitglieder_ajax[mitglied_id]=514'
,'https://coiffeursearch.ch/index.php?L=0&type=999&tx_klinkcosumitglieder_ajax[controller]=Salon&tx_klinkcosumitglieder_ajax[action]=detailjson&tx_klinkcosumitglieder_ajax[mitglied_id]=3707'
    ]

    def parse(self, response):
         jsonresponse = json.loads(response.text)

         item = MyItem()
         item["email"] = jsonresponse["email"]   
         return item
