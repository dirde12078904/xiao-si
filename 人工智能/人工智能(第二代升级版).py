print('----------本产品是基于人工智能第二代,在计算能力上有了进一步提升-邵宗贤----------')
import requests
import pyttsx3
import os as o
print(o)
w=1
engline = pyttsx3.init()
engline.setProperty('voice','zh')

line1 = '你好，主人'
line2 = '欢迎回来'
line3 = '我是小思'
line4 = '您的AI人工智能语言帮手'
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
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
int (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello,Windows")
engine.say('nie,hao')
engine.runAndWait()
engine.stop()


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello,Windows")
engine.say('nie,hao')
engine.runAndWait()
engine.stop()


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print('再见')


