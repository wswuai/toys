# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    ASIN = scrapy.Field()
    rate = scrapy.Field()
    url = scrapy.Field()
    details = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
