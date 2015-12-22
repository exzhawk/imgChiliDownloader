# -*- coding: utf-8 -*-
BOT_NAME = 'imgChili'
SPIDER_MODULES = ['imgChili.spiders']
NEWSPIDER_MODULE = 'imgChili.spiders'
USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/53'
    '7.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36'
)
IMAGES_STORE = 'R:\\'
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
