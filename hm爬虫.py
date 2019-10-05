import requests
import os
import time
import re


#要找的网址
URL = 'https://www.simply-hentai.com/tag/color/page/'

#i为页码
for i in range (1 , 50) :
    #第几页的网址
    url = URL + str(i)
    text = requests.get(url).text

    mangas_urls = re.findall('<a class="js-overview-link" href="(.*?)">', text)
    mangas_names = re.findall('<a class="js-overview-link" href=".*?">(.*?)</a></h3>', text)

    for j in range (0 , len(mangas_urls)) :
        mangas_url = mangas_urls[j] + '/all-pages'

        mangas_name = re.sub('[?|><*/]', '', mangas_names[j])

        print(mangas_name)

        if os.path.exists('D:/爬虫计划/%s' % mangas_name) :
            print("已经有了，跳过")
            continue

        os.makedirs('D:/爬虫计划/%s' % mangas_name)

        #print(mangas_url)

        mangas_text = requests.get(mangas_url).text

        #print(mangas_text)

        pic_urls = re.findall('"path":"(.*?)"' , mangas_text)

        #print(pic_urls)

        cnt = 1
        for i in pic_urls :
            print(i)
            pic_text = requests.get(i).text
            pic_name = str(cnt) + '.jpg'
            cnt += 1
            pic_url = re.findall('&quot;full&quot;:&quot;(.*?)&quot;', pic_text)
            if len(pic_url) == 0 :
                continue
            end_url = pic_url[0]
            image = requests.get(end_url).content
            with open(f'D:/爬虫计划/{mangas_name}/%s' % pic_name , 'wb') as file:
                    file.write(image)
        time.sleep(5)
