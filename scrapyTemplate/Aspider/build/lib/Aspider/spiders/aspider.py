# -*- coding: utf-8 -*-
#from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Aspider.items import AspiderItem


def delete_space_foreach(lis):
    d = lambda x:x .replace(' ','') .replace('\t','') .replace('\n','')


    if(type(lis) == list):
        lis = map(d,lis)
        lis = filter(lambda x:len(x)>0, lis)
        return lis
    else:
        return d(lis)


class AspiderSpider(CrawlSpider):
    name = 'aspider'
    allowed_domains = ['amazon.com']
    start_urls =  ['http://www.amazon.com/']

    def start_requests(self):
        if self.settings['START_URL'] is not None:
            self.logger.info(  "settings found!")
            for i in self.settings['START_URL']:
                yield self.make_requests_from_url(i)
        else:
            self.logger.info(  "settings not found!")
            for i in self.start_urls:
                yield self.make_requests_from_url(i)


    rules = (
        Rule(LinkExtractor(allow=r'.*\/dp\/.*'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=r'.*'), follow=True),
    )

    def parse_item(self, response):
        i = AspiderItem()
        if None == response.xpath('//span[@id="productTitle"]/text()').extract():
            return None
        try:
            i['name']= response.xpath('//head/title/text()').extract()[0]
        except Exception:
            self.logger.warning("cannot find name, skip." + response.request.url)
            return

        i['rate']= response.xpath('//div[@id="avgRating"]/span/text()').extract()
        if len(i['rate'])>0:
            i['rate'] = i['rate'][0]

        i['url']= response.request.url
        i['ASIN'] = response.request.url.split(r'/')[-1]
        i['price'] = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract()


        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        i['details'] = response.xpath('//div[@id="feature-bullets"]/ul/li/span/text()').extract()
        i['category'] = delete_space_foreach(response.xpath('//div[@id="wayfinding-breadcrumbs_feature_div"]/ul/li/span/a/text()').extract())
        #i['details'] = map(
        #    lambda x: x.replace(' ','')
        #    .replace('\t','')
        #    .replace('\n','')
        #    ,i['details'])

        #i['details'] = filter(
        #    lambda x: len(x) > 1
        #    ,i['details']
        #)

        #i['details'] = "\n" .join(i['details'])


        #self.logger.info("crawled : " + i['name'])
        return i
