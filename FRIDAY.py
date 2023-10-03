import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser
import ctypes
import psutil
import pyautogui
import os
import sys
import subprocess
import random


chrome_path ='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('E7Q874-J4279K73X4')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")

    elif hour <= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    speak("FRIDAY Here sir !. How may i help you ?")

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n",)

    except Exception as e:
        print("Please say that Again...!")
        return takeCommand()
    return query


if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'open youtube' in query:
            speak('ok, opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")          

        elif 'open github' in query:
            webbrowser.open("github.com")   

        elif 'open facebook' in query:
            speak('sure thing!')
            webbrowser.open("facebook.com")

        elif 'open chrome' in query:
            speak('okay !')
            os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')

        elif 'open mozilla' in query:
            speak('okay !, opening')   
            os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

        elif 'open microsoft word' in query:
            speak('sure thing!')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016.lnk')    

        elif 'charge' in query or 'power' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent) 
            time_left = secs2hours(battery.secsleft)
            print (percent)
            if percent < 40:
                speak('sir, please connect charger because i can survive only '+ time_left)
            if percent > 40:
                speak("sir, no need to connect the charger because i can survive "+ time_left)
            else:
                speak("don't worry sir, charger is connected")    

        elif 'play music' in query:
            speak('Sure !')
            music_dir = 'E:\\My StUFfs\\Songs\\;)'
            songs = os.listdir(music_dir)
            random_songs = music_dir + random.choice(songs) + '.mp3'
            os.startfile(os.path.join(music_dir, songs))

        elif 'lock' in query:
            speak('As You Wish')
            ctypes.windll.user32.LockWorkStation()

        elif 'screenshot' in query:
            speak('ok sir, let me take a snap')
            pic = pyautogui.screenshot()
            speak('ok it\'s done, i saved it in your desktop')
            pic.save('C:\\Users\\midhu\\Desktop\\Screenshot.png')     

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine !', 'Nice !', 'I am nice and full of energy']
            speak(random.choice(stMsgs))   

        elif 'hello' in query or 'friday' in query:
            speak('Yes sir !, What can i do for you ? ')   

        elif 'name'  in query:
            speak('My name is FRIDAY')    

        elif 'who made you' in query:
            speak ("I was created by Midhun Mohanan")    

        elif 'bye' in query or 'take rest' in query:
            speak('Bye sir !, have a great day !')
            sys.exit()

        else:
            query = query
            print("...")
            speak("Searching")
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    print(results)
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('According to wikipedia - ')
                    print(results)
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
