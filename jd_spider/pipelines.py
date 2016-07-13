# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb.cursors
from twisted.enterprise import adbapi

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy import log
import chardet

SETTINGS = get_project_settings()


class MySQLPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        # Instantiate DB
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host=SETTINGS['DB_HOST'],
                                            user=SETTINGS['DB_USER'],
                                            passwd=SETTINGS['DB_PASSWD'],
                                            port=SETTINGS['DB_PORT'],
                                            db=SETTINGS['DB_DB'],
                                            charset='utf8',
                                            use_unicode=True,
                                            cursorclass=MySQLdb.cursors.DictCursor
                                            )
        self.stats = stats
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        """ Cleanup function, called after crawing has finished to close open
            objects.
            Close ConnectionPool. """
        self.dbpool.close()

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._insert_record, item)
        query.addErrback(self._handle_error)
        return item

    def _insert_record(self, tx, item):
        ID = item['ID'][0]
        name = item['name'][0]
        comment_num = str(item['comment_num'])
        shop_name = item['shop_name'][0]
        link = item['link'][0]
        commentVersion = str(item['commentVersion'])
        commentVersion = commentVersion[1:-1]

        score1count = str(item['score1count'])
        score2count = str(item['score2count'])
        score3count = str(item['score3count'])
        score4count = str(item['score4count'])
        score5count = str(item['score5count'])

        price = str(item['price'])

        ID = ID.encode('utf-8')
        name = name.encode('utf-8')
        comment_num = comment_num.encode('utf-8')
        shop_name = shop_name.encode('utf-8')
        link = link.encode('utf-8')
        commentVersion = commentVersion.encode('utf-8')
        score1count = score1count.encode('utf-8')
        score2count = score2count.encode('utf-8')
        score3count = score3count.encode('utf-8')
        score4count = score4count.encode('utf-8')
        score5count = score5count.encode('utf-8')
        price = price.encode('utf-8')

        sql = "INSERT INTO goods VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (ID, name, comment_num, shop_name, link, commentVersion, score1count, score2count, score3count,
               score4count, score5count, price)
        tx.execute(sql)
        # sql = "INSERT INTO goods (ID, name, comment_num, shop_name, link)" \
        #       "VALUES (%s, %s, %s, %s, %s)" % (ID, name, comment_num, shop_name, link)
        # tx.execute(sql)
        print "yes"

    def _handle_error(self, e):
        log.err(e)


class CommentPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.stats)

    def __init__(self, stats):
        # Instantiate DB
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            host=SETTINGS['DB_HOST'],
                                            user=SETTINGS['DB_USER'],
                                            passwd=SETTINGS['DB_PASSWD'],
                                            port=SETTINGS['DB_PORT'],
                                            db=SETTINGS['DB_DB'],
                                            charset='utf8',
                                            use_unicode=True,
                                            cursorclass=MySQLdb.cursors.DictCursor
                                            )
        self.stats = stats
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        """ Cleanup function, called after crawing has finished to close open
            objects.
            Close ConnectionPool. """
        self.dbpool.close()

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._insert_record, item)
        query.addErrback(self._handle_error)
        return item

    def _insert_record(self, tx, item):
        user_name = item['user_name']
        user_ID = item['user_ID']
        userProvince = item['userProvince']
        content = item['content']
        good_ID = item['good_ID']
        good_name = item['good_name']
        date = item['date']
        replyCount = item['replyCount']
        score = item['score']
        status = item['status']
        title = item['title']
        userRegisterTime = item['userRegisterTime']
        productColor = item['productColor']
        productSize = item['productSize']
        userLevelName = item['userLevelName']
        isMobile = item['isMobile']
        days = item['days']
        tags = item['commentTags']

        # user_name = user_name.encode('utf-8')
        # userProvince = userProvince.encode('utf-8')
        # content = content.encode('utf-8')
        # good_ID = good_ID.encode('utf-8')
        # good_name = good_name.encode('utf-8')
        # date = date.encode('utf-8')
        # title = title.encode('utf-8')
        # userRegisterTime = userRegisterTime.encode('utf-8')
        # productColor = productColor.encode('utf-8')
        # productSize = productSize.encode('utf-8')
        # userLevelName = userLevelName.encode('utf-8')
        # tags = tags.encode('utf-8')

        sql = "INSERT INTO comment1 VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'," \
              "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (user_name, user_ID, userProvince, content, good_ID, good_name, date, replyCount, score,
               status, title, userRegisterTime, productColor, productSize, userLevelName,
               isMobile, days, tags)

        # print "user_name"
        # print user_name
        # print "user_ID"
        # print user_ID
        # print "userProvince"
        # print userProvince
        # print "content"
        # print content
        # print "good_ID"
        # print good_ID
        # print "good_name"
        # print good_name
        # print "date"
        # print date
        # print "replyCount"
        # print replyCount
        # print "score"
        # print score
        # print "status"
        # print status
        # print "title"
        # print title
        # print "userRegisterTime"
        # print userRegisterTime
        # print "productColor"
        # print productColor
        # print "productSize"
        # print productSize
        # print "userLevelName"
        # print userLevelName
        # print "isMobile"
        # print isMobile
        # print "days"
        # print days
        # print "tags"
        # print tags
        # print sql
        tx.execute(sql)
        print "yes"

    def _handle_error(self, e):
        log.err(e)
