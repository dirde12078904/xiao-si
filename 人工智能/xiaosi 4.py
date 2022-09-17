print('-------------------------本产品是邵宗贤独家制作,人工智能-小思2022年的第4代的产物-----------------------')
print('人工智能小思-第四代-九月版')
import requests
import pyttsx3
print('你好,我是小思')
print('第四代人工智能')
engline = pyttsx3.init()
engline.setProperty('voice','zh')
line1 = '你好，主人'
line2 = '欢迎光临'
line3 = '我是小思'
line4 = '您的第四代人工智能'
line5 = '欢迎为您服务'
engline.say(line1)
engline.say(line2)
engline.say(line3)
engline.say(line4)
engline.say(line5)
engline.runAndWait()

class Turing_robot(object):
    while True:
      a=input()
      url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
      te=requests.get(url).json()
      data=te['data']['info']['text']
      print(data)
      ini= pyttsx3.init()
      shuo = ini.say(data)
      ini.runAndWait()
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 125)
int (volume)
engine.setProperty('volume',1.0)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)

engine.say("Hello,Windows")
engine.say('nie,hao')
engine.runAndWait()
engine.stop()


""" RATE"""
rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 125)


"""VOLUME"""
volume = engine.getProperty('volume')
print (volume)
engine.setProperty('volume',1.0)

"""VOICE"""
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

print('再见')
print('欢迎下次光临')
print('------------------------------')