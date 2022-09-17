print('-------------------------本产品是邵宗贤独家制作,人工智能-小思2022年的第5代的产物-----------------------')
print('--人工智能小思从10月份开始,以人工智能系统改为小思网络操作系统-9月份出版')
import json
import socket
import pyttsx3
import requests
import socket
import uuid
from urllib.request import urlopen, Request
from urllib.parse import urlencode
print('你好,我是小思')
print('第五代人工智能')
engline = pyttsx3.init()
engline.setProperty('voice','zh')
line1 = '你好，主人'
line2 = '欢迎光临'
line3 = '我是小思同学'
line4 = '小思的第五代产品(fifth generation)'
line5 = '欢迎为您服务'
engline.say(line1)
engline.say(line2)
engline.say(line3)
engline.say(line4)
engline.say(line5)
engline.runAndWait()
class Turing_robot(object):
    while True:
            a = input()
            url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' %a
            te = requests.get(url).json()
            data = te['data']['info']['text']
            print(data)
            ini = pyttsx3.init()
            shuo = ini.say(data)
            ini.runAndWait()

def getTuringText(self,text):
    user_ip = self.getHostIP()
    mac_id = self.getMacID()
    turing_url_data = dict(key=self.app_key,info=text,userid=mac_id)
def getHostIP(self):
    socket_info = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    socket_info.connect('8.8.8.8', 80)
    ip = socket_info.getsockname()[0]
    return ip
def getMaID(self):
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac
