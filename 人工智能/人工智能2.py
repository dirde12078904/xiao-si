import requests
import pyttsx3
print('请输入你想说的：')
while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
    ini= pyttsx3.init()
    shuo=ini.say(data)
    

