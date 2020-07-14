from selenium import webdriver

browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()
browser1.get('http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?isArea=0&repairLd=')

for page in range(1 , 359) :
    print(page)
    input = browser1.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/ul/li/div[1]/a')
    while True :
        if len(input) == 0 :
            browser1.back()
            browser1.find_elements_by_xpath('/ html / body / div[4] / div / div[1] / div / div[3] / a')[-2].click()
            input = browser1.find_elements_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/ul/li/div[1]/a')
            continue
        else :
            break
    for i in input :
        url = i.get_attribute('href')
        while True :
            try :
                browser2.get(url)
            except :
                continue
            else :
                break
        Hazard_level = browser2.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[2]/a').text
        Vulnerability_types = browser2.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[4]/a').text
        Threat_types = browser2.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[6]/a').text

        if len(Hazard_level) == 0:
            continue
        add = 'C:/Users/14714/Desktop/py/等级.txt'
        f = open(add, 'a')
        f.write(Hazard_level + '\n')
        if len(Vulnerability_types) != 0:
            add = 'C:/Users/14714/Desktop/py/vu/' + Hazard_level + '.txt'
            f = open(add, 'a')
            f.write(Vulnerability_types + '\n')
        if len(Threat_types) != 0:
            add = 'C:/Users/14714/Desktop/py/th/' + Hazard_level + '.txt'
            f = open(add, 'a')
            f.write(Threat_types + '\n')

        print(Hazard_level)
        print(Vulnerability_types)
        print(Threat_types)
    browser1.find_elements_by_xpath('/ html / body / div[4] / div / div[1] / div / div[3] / a')[-2].click()
