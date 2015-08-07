# -*- coding: utf-8 -*-
#import scrapy
#from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule

#from Aspider.items import AspiderItem

import logging
logger = logging.getLogger(__name__)
import aspider


def delete_space_foreach(lis):
    d = lambda x:x .replace(' ','') .replace('\t','') .replace('\n','')


    if(type(lis) == list):
        lis = map(d,lis)
        lis = filter(lambda x:len(x)>0, lis)
        return lis
    else:
        return d(lis)


class AspiderSpider(aspider.AspiderSpider):
    name = 'cnaspider'
    allowed_domains = ['amazon.cn']
    start_urls = ['http://www.amazon.cn/']
