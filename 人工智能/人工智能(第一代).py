print('-------------------------本产品是邵宗贤独家制作,人工智能-小思2021年-12月的第1代的产物-----------------------')
import requests
while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)