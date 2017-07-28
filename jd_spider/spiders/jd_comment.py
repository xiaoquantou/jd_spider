# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from jd_spider.items import commentItem
import json
import xlrd


class comment_spider(Spider):
    name = "comment"
    xlrd.Book.encoding = "utf-8"
    data = xlrd.open_workbook("goods.xls")
    # goods为要抓取评论的商品信息，现提供一个goods.xls文件供参考,第1列：商品ID；第2列：商品评论数；第3列：商品的commentVersion
    # test.xlsx也可以使用
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    good_id = table.col_values(0)  # 商品ID
    comment_n = table.col_values(1)  # 商品评论数
    comment_V = table.col_values(2)  # 商品评论的commentVersion

    start_urls = []
    for i in range(len(good_id)):  # 一件商品一件商品的抽取
        good_num = int(good_id[i])
        comment_total = int(comment_n[i])
        if comment_total % 10 == 0:  # 算出评论的页数，一页10条评论
            page = comment_total/10
        else:
            page = comment_total/10 + 1
        for k in range(0, page):
            url = "http://sclub.jd.com/productpage/p-" + str(good_num) + "-s-0-t-3-p-" + str(k) \
                  + ".html?callback=fetchJSON_comment98vv" + str(comment_V[i])
            start_urls.append(url)

    def parse(self, response):
        temp1 = response.body.split('productAttr')
        str = '{"productAttr' + temp1[1][:-2]
        str = str.decode("gbk").encode("utf-8")
        js = json.loads(unicode(str, "utf-8"))
        comments = js['comments']  # 该页所有评论

        items = []
        for comment in comments:
            item1 = commentItem()
            item1['user_name'] = comment['nickname']
            item1['user_ID'] = comment['id']
            item1['userProvince'] = comment['userProvince']
            item1['content'] = comment['content']
            item1['good_ID'] = comment['referenceId']
            item1['good_name'] = comment['referenceName']
            item1['date'] = comment['referenceTime']
            item1['replyCount'] = comment['replyCount']
            item1['score'] = comment['score']
            item1['status'] = comment['status']
            title = ""
            if comment.has_key('title'):
                item1['title'] = comment['title']
            item1['title'] = title
            item1['userRegisterTime'] = comment['userRegisterTime']
            item1['productColor'] = comment['productColor']
            item1['productSize'] = comment['productSize']
            item1['userLevelName'] = comment['userLevelName']
            item1['isMobile'] = comment['isMobile']
            item1['days'] = comment['days']
            tags = ""
            if comment.has_key('commentTags'):
                for i in comment['commentTags']:
                    tags = tags + i['name'] + " "
            item1['commentTags'] = tags
            items.append(item1)
        return items