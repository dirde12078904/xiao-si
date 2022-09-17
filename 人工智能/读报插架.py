import pyttsx3
engline = pyttsx3.init()
engline.setProperty('voice','zh')
line1 = '你好,Windows'
print('你好 windows')
engline.say(line1)
engline.runAndWait()