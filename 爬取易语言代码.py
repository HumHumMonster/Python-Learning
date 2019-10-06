import  urllib.request
from lxml import etree


url = 'http://www.eyuyan.la/cate/6-1.html'


page_source = etree.HTML(urllib.request.urlopen(url).read().decode("utf-8"))

#page_total = page_source.xpath('//*[@class = "pg"]/label/span/text()')

page_total = int(page_source.xpath('//div[@class = "pg"]/label/span/text()')[0].split()[1])

content_list = page_source.xpath('//div[@class = "cate_list"]/ul/li/a/@href')

#print (page_source)

#print(content_list)

for eve_content_url in content_list :
    content_url = 'http://www.eyuyan.la' + eve_content_url
    #print(content_url)
    content_page_souce = etree.HTML(urllib.request.urlopen(content_url).read().decode("utf-8"))
    title = content_page_souce.xpath('//h1/text()')[0].split()[0]
    print (title)
    download_url = content_page_souce.xpath('//div[@class = "article_neirong"]//a/@href')[0]
    end_url = 'http://www.eyuyan.la' + download_url
    #print (download_url)
    print (end_url)
