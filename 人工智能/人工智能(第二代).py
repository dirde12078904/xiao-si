print('-------------------------本产品是邵宗贤独家制作,人工智能-小思2021年-4月的第2代的产物-----------------------')
print('----------本产品比第一代更加有人性化,基于(人工智能1.1)----------')
import requests
import pyttsx3
engline = pyttsx3.init()
engline.setProperty('voice','zh')

line1 = '你好，主人'
line2 = '欢迎回来'
line3 = '我是小思'
line4 = '您的AI第二代人工智能语言帮手'
line5 = '欢迎为您服务'
engline.say(line1)
engline.say(line2)
engline.say(line3)
engline.say(line4)
engline.say(line5)
engline.runAndWait()
print('你好,我是小思')
print('欢迎为您服务')
while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
    ini= pyttsx3.init()
    shuo=ini.say(data)
    ini.runAndWait()

