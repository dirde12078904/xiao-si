print('-------------------------本产品是邵宗贤独家制作,人工智能-小思2022-1月的第1代附加产物-----------------------')
import pyttsx3
import io
import sys
print(io)
print(sys)
engline = pyttsx3.init()
engline.setProperty('voice','zh')

line1 = '你好，主人'
line2 = '欢迎回来'
line3 = 'Hello~~~ windows'
line4 = '我是AI人工智能小思1.1版本'
line5 = '您有什么需要帮助的'

engline.say(line1)
engline.say(line2)
engline.say(line3)
engline.say(line4)
engline.say(line5)
engline.runAndWait()

