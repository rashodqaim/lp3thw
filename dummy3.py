# def say_hello(name = "Kyle"):
#     print(f"hello {name}")

# say_hello("Rashod")
# # say_hello




# from gtts import gTTS
# import os

# mytext = "Good Morning"

# myobj = gTTS(text=mytext, lang='en', slow=False)
# print(myobj)
# myobj.save("test.mp3")
# os.system("start test.mp3")


import pyttsx3
engine = pyttsx3.init()
engine.say("You are a genius for figuring this out")
engine.runAndWait()