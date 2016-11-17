# -*-coding:utf-8-*-
import urllib2
from lxml import etree

'''
dst="http://www.ftchinese.com"
html = urlopen(dst,'lmxl')
tree = etree.parse(html)
result = tree.xpath('//h2[@class="item-headline"]/a')
print result
'''

request = urllib2.Request("http://www.ftchinese.com")
response = urllib2.urlopen(request)
html = response.read()
page = etree.HTML(html)
#wholeHtml = etree.tostring(page)

result = page.xpath('//h2[@class="item-headline"]/a')
for i in result:
    print i.text
