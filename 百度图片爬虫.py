
s = input("输入查找的信息")

#确定url
url = f'https://image.baidu.com/search/flip?tn=baiduimage8&word={s}'

import requests
import re
text = requests.get(url).text

#print(text)

image_urls = re.findall('"objURL":"(.*?)"' , text)

for image_url in image_urls :

    image_name = image_url.split('/')[-1]
    # $表示匹配字符串的末尾
    image_result = re.search('(.jpg|.png|.jpeg|.tif|.gif|.ico)$' , image_name)

    if image_result == None :
        image_name = image_name + '.jpg'

    print(image_name)

    image = requests.get(image_url).content

    with open('./test/%s' % image_name , 'wb') as file :
        file.write(image)
