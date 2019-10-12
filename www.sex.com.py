'''
目标网址：https://www.sex.com/search/pics?query=uniform&sort=popular-all&page=2
程序目的：爬取所有图片
时间：2019-10-12
作者：HumHumMonster
V：1.0
'''

import  urllib.request
from lxml import etree
import requests
import requests

cnt = 1 #图片名
#浏览器输入about://version
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}   #伪装浏览器

for page_num in range(1 , 5) :
    url = 'https://www.sex.com/search/pics?query=uniform&sort=popular-all&page=' + str(page_num)
    #print("url = ")
    #print(url)
    req = urllib.request.Request(url, headers=headers)
    text = urllib.request.urlopen(req).read().decode("utf-8")
    page_source = etree.HTML(text)
    list = page_source.xpath('//a[@class="image_wrapper"]/@href')
    for i in list :
        print('https://www.sex.com' + i)
        img_req = urllib.request.Request('https://www.sex.com' + i, headers=headers)
        img_text = urllib.request.urlopen(img_req).read().decode("utf-8")
        img_page_source = etree.HTML(img_text)
        end_urls = img_page_source.xpath('/html/body/div[8]/div/div[1]/div[1]/div[2]/div[2] / a / img / @src')
        if (len(end_urls) == 0) :
            end_urls = img_page_source.xpath('//div[@class = "image_frame"] / img / @ src')
        if (len(end_urls) == 0):
            print("NOT FOUND")
            continue
        end_url = end_urls[0]
        print(end_url)

        image = requests.get(end_url, headers=headers).content
        pic_name = str(cnt) + '.jpeg'
        with open('D:/爬虫计划/uniform/%s' % pic_name, 'wb') as file:
            file.write(image)
        cnt += 1
    break
