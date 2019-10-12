'''

目标网址：https://hentai-cosplay.com/ranking-images/page/
程序目的：爬取所有图片

时间：2019-10-12
作者：HumHumMonster

V：1.0

'''


import  urllib.request
from lxml import etree
import requests
import requests


cnt = 601   #图片名
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}   #伪装浏览器

for page_num in range(7 , 101) :
    url = 'https://hentai-cosplay.com/ranking-images/page/' + str(page_num) + '/'

    req = urllib.request.Request(url , headers=headers)

    text = urllib.request.urlopen(req).read().decode("utf-8")

    #print(text)

    page_source = etree.HTML(text)

    list = page_source.xpath('//div[@class="item icon-overlay"]/a[1]/@href')

    for i in list :
        print('https://hentai-cosplay.com' + i)
        img_req = urllib.request.Request('https://hentai-cosplay.com' + i, headers=headers)
        img_text = urllib.request.urlopen(img_req).read().decode("utf-8")
        img_page_source = etree.HTML(img_text)
        end_urls = img_page_source.xpath('//*[@id="display_image_detail"]/p/a/img/@src')
        print(end_urls)
        if (len(end_urls) == 0) :
            print("NOT FOUND")
            continue
        end_url = end_urls[0]
        print(end_url)
        image = requests.get(end_url , headers = headers).content
        pic_name = str(cnt) + '.jpg'
        with open('D:\爬虫计划\cosplay\%s' % pic_name , 'wb') as file :
            file.write(image)
        cnt += 1
