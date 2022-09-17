import pyttsx3
import requests
print('----------此版本解决了人工智能第一代的网络卡顿和延迟,加入了最新的人工智能库(os库:提供通用的、基本的操作系统交互功能),邵宗贤作-2022')
print('你好,我是小思')
print('欢迎为您服务')
engline = pyttsx3.init()
engline.setProperty('voice','zh')
line1 = '你好，主人'
line2 = '欢迎回来'
line3 = '我是小思'
line4 = '您的AI第一代加强版人工智能语言帮手'
line5 = '欢迎为您服务'
engline.say(line1)
engline.say(line2)
engline.say(line3)
engline.say(line4)
engline.say(line5)
engline.runAndWait()
while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)