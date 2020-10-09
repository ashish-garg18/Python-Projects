# install libraries pip install pyttsx3 and pip install pywin32

import pyttsx3

data = input("Enter the text to convert to Speech")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()