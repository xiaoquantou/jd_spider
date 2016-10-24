# jd_spider

用scrapy框架写的京东爬虫，可以抓取京东商品信息和评论

# 1、目的：
<li>1、爬取京东的商品信息（以电子烟为例）</li>
<li>2、爬取商品的评论信息</li>

#2、抓取到的数据属性如下所示
<br>
##商品数据
<br>
![image](http://img.blog.csdn.net/20160706175045922)
<br>
##评论数据
<br>
![image](http://img.blog.csdn.net/20160706174754513)
<br>
#3、使用说明：
##(1)抓取商品信息和抓取评论分别写在了两个不同的爬虫里

<p>抓取商品信息代码在jd_home.py中，数据库在setting.py中修改ITEM_PIPELINES，使用MySQLPipeline</p>
<p>抓取评论代码在jd_comment.py中，数据库在setting.py中修改ITEM_PIPELINES，使用CommentPipeline</p>

##(2)setting.py文件
<p>默认开启了代理IP，因为IP的存活期的限制，要定期更新PROXIES中IP信息，可从网站：http://www.xicidaili.com/ 中找免费的代理IP</p>

<p>如果不想使用代理IP，可以将DOWNLOADER_MIDDLEWARES代码注释掉</p>

<p>数据库的配置：<p>
<li>setting.py中可以配置数据库的主机，端口，用户名，密码和数据库名信息</li>
<li>pipeline.py中在sql语句中配置你要存入的表的名称。</li>
<li>数据库表结构：</li>
<li>jd_comment.sql：评论数据</li>   
<li>jd_goods.sql：商品数据</li>

<br>
<p>在使用本爬虫中，因为在抓取评论信息时需要用到goods.xls文件。因此需要先抓取商品信息，然后将商品信息的相关内容导出到goods.xls中（这里提供了一个goods.xls的格式供参考）</p>
<p>goods.xls格式：第1列：商品ID，第2列：商品评论数；第3列：商品的commentVersion</p>
<p>在一个工程中，抓取商品信息和抓取评论信息不能同时进行。</p>
<br>
<p>更多爬虫的细节可以参考我的博客文章：</p>
<li>http://blog.csdn.net/xiaoquantouer/article/details/51840332</li>

<li>http://blog.csdn.net/xiaoquantouer/article/details/51841016</li>

<br>
##有问题欢迎留言


