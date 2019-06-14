# -*- coding: utf-8 -*-

# settings.py

SPIDER_MODULES = ['mutil_spider.spiders']
NEWSPIDER_MODULE = 'mutil_spider.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
#    'Sina.pipelines.SinaPipeline': 300,
#     'scrapy_redis.pipelines.RedisPipeline': 400,
    'mutil_spider.pipelines.SinaPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

REDIS_URL = 'redis://root:123456@192.168.1.100:6379'


# MONGODB 主机
MONGODB_HOST = '192.168.1.100'
# 端口号，默认是27017
MONGODB_PORT = 27017
# 设置数据库名称
MONGODB_DBNAME = 'sina'
# 存放本次数据的表名称
MONGODB_DOCNAME = 'news'







