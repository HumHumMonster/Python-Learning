
cnt = 1

s = input("输入查找的信息")

#确定url
url = f'https://image.baidu.com/search/flip?tn=baiduimage8&word={s}'

import requests
import re



while (url != None) :
    text = requests.get(url).text

    #print(text)

    image_urls = re.findall('"objURL":"(.*?)"' , text)

    for image_url in image_urls :

        image_name = str(cnt) + '.jpg'
        cnt += 1
        print(cnt)
        image = requests.get(image_url).content

        with open('./test/%s' % image_name , 'wb') as file :
            file.write(image)

    url = 'https://image.baidu.com/' + re.findall('a href="(.*?)" class="n">下一页' , text)[0]
    print(url)
