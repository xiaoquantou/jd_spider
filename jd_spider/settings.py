# -*- coding: utf-8 -*-

# Scrapy settings for jd_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_spider'

SPIDER_MODULES = ['jd_spider.spiders']
NEWSPIDER_MODULE = 'jd_spider.spiders'

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# http://www.xicidaili.com/
PROXIES = [
    {'ip_port': '202.75.210.45:7777', 'user_pass': ''},
    {'ip_port': '222.211.65.72:8080', 'user_pass': ''},
    {'ip_port': '121.33.226.167:3128', 'user_pass': ''},
    {'ip_port': '121.40.108.76:80', 'user_pass': ''},
    {'ip_port': '122.96.59.102:83', 'user_pass': ''},
    {'ip_port': '118.114.77.47:8080', 'user_pass': ''},
    {'ip_port': '222.80.95.119:1337', 'user_pass': ''},
    {'ip_port': '112.91.208.78:9999', 'user_pass': ''},
    {'ip_port': '122.226.128.251:3128', 'user_pass': ''},
    {'ip_port': '218.27.204.114:9797', 'user_pass': ''},
    {'ip_port': '58.67.159.50:80', 'user_pass': ''},
    {'ip_port': '110.206.127.136:9797', 'user_pass': ''},
    {'ip_port': '220.249.185.178:9999', 'user_pass': ''},
    {'ip_port': '122.225.106.36:80', 'user_pass': ''},
    {'ip_port': '113.200.214.163:9999', 'user_pass': ''},
]

COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    'jd_spider.middlewares.RandomUserAgent': 1,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'jd_spider.middlewares.ProxyMiddleware': 100,
}

DOWNLOAD_DELAY = 7

LOG_LEVEL = 'INFO'

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWD = 'U7i8o9p0'
DB_DB = 'test'

ITEM_PIPELINES = {
    # 'jd_spider.pipelines.MySQLPipeline': 300,
    'jd_spider.pipelines.CommentPipeline': 300,
}
