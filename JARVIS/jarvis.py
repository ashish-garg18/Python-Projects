import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("Welcome Back")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f"The current time is {Time}")

time()

def wiki():
    query = search
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

def takeCommand():
    speak("What do you want to search ?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-ln')
        print(f"You said : {query}\n")
    except Exception as e:
        print(e)
        print("Say that Again..")
        speak("Say that Again..")
        return "None"
    return query

search = takeCommand()
wiki()


