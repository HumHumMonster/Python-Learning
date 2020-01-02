import requests
from lxml import etree



class Login(object) :
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/login' ,
            'Sec-Fetch-Mode': 'navigate' ,
            'Sec-Fetch-Site': 'same-origin' ,
            'Sec-Fetch-User': '?1' ,
            'Upgrade-Insecure-Requests': '1' ,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.ligined_url = 'https://github.com/settings/profile'
        # requests库的Session可以帮我们维持一个会话。
        self.session = requests.Session()

    # 获得authenticity_token
    def token(self):
        response = self.session.get(self.login_url , headers = self.headers)
        selector = etree.HTML(response.text)
        # etree模块可以自动修正HTML文本
        token = selector.xpath('//*[@id="login"]/form/input[2]/@value')[0]
        return token

    def login(self , email , password):
        post_data = {
            'commit': 'Sign in' ,
            'utf8': '✓' ,
            'authenticity_token': self.token() ,
            'login': '你的账号' ,
            'password': '你的密码'
        }



        self.session.post(self.post_url , data = post_data , headers = self.headers)
        response = self.session.get(self.ligined_url , headers = self.headers)
        print(response.status_code)
        selector = etree.HTML(response.text)
        result = etree.tostring(selector)
        print(result.decode('utf-8'))

        name = selector.xpath('//*[@id="user_profile_name"]/@value')[0]
        print(name)





if __name__ == "__main__" :
    login = Login()
    login.login(email="1471427006@qq.com" , password='password')
