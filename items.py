# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShiyanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    money= scrapy.Field()
    typee = scrapy.Field()
    dizhi = scrapy.Field()
    #maijia = scrapy.Field()
    name = scrapy.Field()
    #pass
