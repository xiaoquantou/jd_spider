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

# 这里使用的代理IP，因为IP的存活期的限制，请定期更新下面的IP，可从http://www.xicidaili.com/ 中找免费的代理IP
PROXIES = [
    {'ip_port': '202.108.2.42:80', 'user_pass': ''},
    {'ip_port': '122.96.59.104:80', 'user_pass': ''},
    {'ip_port': '120.76.243.40:80', 'user_pass': ''},
    {'ip_port': '139.196.108.68:80', 'user_pass': ''},
    {'ip_port': '60.194.100.51:80', 'user_pass': ''},
    {'ip_port': '202.171.253.72:80', 'user_pass': ''},
    {'ip_port': '123.56.74.13:8080', 'user_pass': ''},
]

COOKIES_ENABLED = False


# 如果不想使用代理IP，可以将下面这段DOWNLOADER_MIDDLEWARES代码注释掉
DOWNLOADER_MIDDLEWARES = {
    'jd_spider.middlewares.RandomUserAgent': 1,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'jd_spider.middlewares.ProxyMiddleware': 100,
}

DOWNLOAD_DELAY = 7  # 下载延迟

LOG_LEVEL = 'INFO'

# 数据库的配置，请将下面的换成你自己的数据库配置
DB_HOST = 'localhost'  # 主机名
DB_PORT = 3306  # 端口号
DB_USER = 'root'    # 用户名
DB_PASSWD = 'xiaoquantou'  # 密码
DB_DB = 'test'  # 数据库名

ITEM_PIPELINES = {
    'jd_spider.pipelines.MySQLPipeline': 300,  # 抓取商品信息时，使用该通道
    # 'jd_spider.pipelines.CommentPipeline': 300,  # 抓取评论信息时，使用该通道
}
