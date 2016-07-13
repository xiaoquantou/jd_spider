# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class goodsItem(Item):
    link = Field()  # 商品链接
    ID = Field()  # 商品ID
    name = Field()  # 商品名字
    comment_num = Field()  # 评论人数
    shop_name = Field()  # 店家名字
    price = Field()  # 价钱
    commentVersion = Field()  # 为了得到评论的地址需要该字段
    score1count = Field()  # 评分为1星的人数
    score2count = Field()  # 评分为2星的人数
    score3count = Field()  # 评分为3星的人数
    score4count = Field()  # 评分为4星的人数
    score5count = Field()  # 评分为5星的人数


class commentItem(Item):
    user_name = Field()  # 评论用户的名字
    user_ID = Field()  # 评论用户的ID
    userProvince = Field()  # 评论用户来自的地区
    content = Field()  # 评论内容
    good_ID = Field()  # 评论的商品ID
    good_name = Field()  # 评论的商品名字
    date = Field()  # 评论时间
    replyCount = Field()  # 回复数
    score = Field()  # 评分
    status = Field()  # 状态
    title = Field()
    userLevelId = Field()
    userRegisterTime = Field()  # 用户注册时间
    productColor = Field()  # 商品颜色
    productSize = Field()  # 商品大小
    userLevelName = Field()  # 银牌会员，钻石会员等
    userClientShow = Field()  # 来自什么 比如来自京东客户端
    isMobile = Field()  # 是否来自手机
    days = Field()  # 天数
    commentTags = Field()  # 标签
