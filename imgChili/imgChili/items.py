# -*- coding: utf-8 -*-
import scrapy


class ImgchiliItem(scrapy.Item):
    image_urls = scrapy.Field()
