# -*- encoding: utf-8 -*-
# Author: Epix
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from imgChili.items import ImgchiliItem


class imgChiliSpider(CrawlSpider):
    name = 'imgChiliSpider'
    allowed_domains = ['imgchili.net']
    rules = (Rule(LinkExtractor(allow=r'show\/.*', restrict_css='div.table_border', deny_extensions=[]),
                  callback='parse_show_page'),)
    start_urls = []
    for line in open('albums.txt'):
        start_urls.append(line.strip())

    def parse_show_page(self, response):
        img_url = response.css('#show_image').xpath('./@src')[0].extract()
        item = ImgchiliItem()
        item['image_urls'] = [img_url]
        yield item
