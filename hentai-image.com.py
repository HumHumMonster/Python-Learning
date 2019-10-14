'''
目标网址：https://hentai-image.com
程序目的：爬取所有图片
时间：2019-10-14
作者：HumHumMonster
V：1.0
'''

import  urllib.request
from lxml import etree
import random
import os
import re
import time
import requests

cnt = 1 #图片名
#浏览器输入about://version
headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}   #伪装浏览器
headers2 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}   #伪装浏览器

for page_num in range(1 , 5) :
    url = 'https://hentai-image.com/ranking/page/' + str(page_num) + '/'
    print(url)
    req = urllib.request.Request(url, headers=headers1)

    text = urllib.request.urlopen(req).read().decode("utf-8")

    page_source = etree.HTML(text)

    list = page_source.xpath(' // *[ @ id = "image-list"] / li / div / div / a / @href')

    for i in list :
        print ('https://hentai-image.com' + i)
        img_req = urllib.request.Request('https://hentai-image.com' + i, headers=headers2)
        img_text = urllib.request.urlopen(img_req).read().decode("utf-8")
        img_page_source = etree.HTML(img_text)
        name = img_page_source.xpath('// *[ @ id = "title"] / h2 / text()')[0]
        name = re.sub('[?|><*/:\']', '', name)
        if (len(name) > 80) :
            name = name[0 : 80]
        print(name)
        if os.path.exists('D:/爬虫计划/hentai_image/%s' % name):
            print("已经有了，跳过")
            continue

        os.makedirs('D:/爬虫计划/hentai_image/%s' % name)
        cnt = 1
        end_url = img_page_source.xpath('// *[ @ id = "display_image_detail"] / div / a[1] / img / @src')[0]
        u = end_url[0 : -5]
        page = 1
        cnt = 1
        while True :
            newu = u + str(page) + '.jpg'
            pic_name = str(cnt)
            try :
                end_req = urllib.request.Request(newu, headers=headers1)
                text = urllib.request.urlopen(end_req).read()
            except urllib.error.HTTPError :
                pass
            else :
                pic_name = pic_name + '.jpg'
                print(newu)
                print(pic_name)
                image = requests.get(newu, headers=headers2).content
                with open(f'D:/爬虫计划/hentai_image/{name}/%s' % pic_name, 'wb') as file:
                    file.write(image)
                cnt += 1
                page += 1
                continue

            newu = u + str(page) + '.jpeg'
            try:
                end_req = urllib.request.Request(newu, headers=headers1)
                text = urllib.request.urlopen(end_req).read()
            except urllib.error.HTTPError:
                pass
            else:
                pic_name = pic_name + '.jpeg'
                print(newu)
                print(pic_name)
                image = requests.get(newu, headers=headers2).content
                with open(f'D:/爬虫计划/hentai_image/{name}/%s' % pic_name, 'wb') as file:
                    file.write(image)
                cnt += 1
                page += 1
                continue

            newu = u + str(page) + '.png'
            try:
                end_req = urllib.request.Request(newu, headers=headers1)
                text = urllib.request.urlopen(end_req).read()
            except urllib.error.HTTPError:
                pass
            else:
                pic_name = pic_name + '.png'
                print(newu)
                print(pic_name)
                image = requests.get(newu, headers=headers2).content
                with open(f'D:/爬虫计划/hentai_image/{name}/%s' % pic_name, 'wb') as file:
                    file.write(image)
                cnt += 1
                page += 1
                continue
            break
