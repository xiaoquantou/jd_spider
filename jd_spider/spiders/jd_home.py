# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from jd_spider.items import goodsItem
from scrapy.selector import Selector
import scrapy
import re
import json


class jd_spider(Spider):
    name = "jd"
    start_urls = []
    for i in range(1, 11):
        url = 'http://list.jd.com/list.html?cat=1672,2599,1440&ev=111217_635585&page=' + str(i)
        start_urls.append(url)

    def parse_price(self, response):
        item1 = response.meta['item']
        temp1 = response.body.split('jQuery([')
        s = temp1[1][:-4]  # 获取到需要的json内容
        # str = str.decode("gbk").encode("utf-8")
        # js = json.loads(unicode(str, "utf-8"))
        js = json.loads(str(s))  # js是一个list
        if js.has_key('pcp'):
            item1['price'] = js['pcp']
        else:
            item1['price'] = js['p']
        return item1

    def parse_getCommentnum(self, response):
        item1 = response.meta['item']
        # response.body是一个json格式的
        js = json.loads(str(response.body))
        # js = json.loads(str)
        # print js['CommentsCount'][0]['Score1Count']
        item1['score1count'] = js['CommentsCount'][0]['Score1Count']
        item1['score2count'] = js['CommentsCount'][0]['Score2Count']
        item1['score3count'] = js['CommentsCount'][0]['Score3Count']
        item1['score4count'] = js['CommentsCount'][0]['Score4Count']
        item1['score5count'] = js['CommentsCount'][0]['Score5Count']
        item1['comment_num'] = js['CommentsCount'][0]['CommentCount']
        num = item1['ID']  # 获得商品ID
        s1 = str(num)
        url = "http://pm.3.cn/prices/pcpmgets?callback=jQuery&skuids=" + s1[3:-2] + "&origin=2"
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_price)
        # return item1
        # print 'ID'
        # print item1['ID'][0]
        # print 'name'
        # print item1['name'][0]
        # print 'comment_num'
        # print item1['comment_num']
        # print 'shop_name'
        # print item1['shop_name'][0]
        # print 'commentVersion'
        # commentVersion = str(item1['commentVersion'])
        # commentVersion = commentVersion[1:-1]
        # print commentVersion
        # print 'link'
        # print item1['link'][0]
        # print 'score1count'
        # print item1['score1count']
        # print 'score2count'
        # print item1['score2count']
        # print 'score3count'
        # print item1['score3count']
        # print 'score4count'
        # print item1['score4count']
        # print 'score5count'
        # print item1['score5count']

    def parse_detail(self, response):
        item1 = response.meta['item']
        sel = Selector(response)
        # item1['comment_num'] = sel.xpath('//div[@id="summary"]//a[@href="#comment"]/text()').extract()

        temp = response.body.split('commentVersion:')
        pattern = re.compile("[\'](\d+)[\']")
        if len(temp) < 2:
            item1['commentVersion'] = -1
        else:
            match = pattern.match(temp[1][:10])
            item1['commentVersion'] = match.group()

        url = "http://club.jd.com/clubservice.aspx?method=GetCommentsCount&referenceIds=" + str(item1['ID'][0])
        yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_getCommentnum)
        # return item
        # print 'ID'
        # print item['ID'][0]
        # print 'name'
        # print item['name'][0]
        # print 'comment_num'
        # print item['comment_num'][0]
        # print 'shop_name'
        # print item['shop_name'][0]
        # print 'commentVersion'
        # commentVersion = str(item['commentVersion'])
        # commentVersion = commentVersion[1:-1]
        # print commentVersion
        # print 'link'
        # print item['link'][0]

    def parse(self, response):  # 解析搜索页
        sel = Selector(response)  # Xpath选择器
        goods = sel.xpath('//li[@class="gl-item"]')
        # print 'goods'
        # print len(goods)  # 总共60条商品信息
        for good in goods:
            item1 = goodsItem()
            item1['ID'] = good.xpath('./div/@data-sku').extract()
            item1['name'] = good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
            item1['shop_name'] = good.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract()
            item1['link'] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()
            # item1['comment_num'] = good.xpath('./div/div[@class="p-commit"]//a/text()').extract()
            url = "http:" + item1['link'][0] + "#comments-list"
            # print detail
            yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_detail)