import time
from datetime import date
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
from pyautogui import click
from keyboard import press
from keyboard import write
import calendar
import pyjokes
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

MASTER = "Tarun"
print("Initializing Inputs...")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak(f"Good morning master...")
    elif 12 <= hour < 17:
        speak(f"Good afternoon master...")

    elif 17 <= hour:
        speak(f"Good Evening master...")

    print('Eva at your service master...')
    speak("Eva at your service master...")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"You said : {query}")
        except Exception :
            print("I didn't get you master")
            speak("I didn't get you master...")
            return "None"
        return query

speak("Initializing Inputs...")
time.sleep(0.5)
print("Importing all preferences...")
speak("Importing all preferences...")
time.sleep(0.5)
print("Getting things ready for you master...")
speak("Getting things ready for you master...")
time.sleep(0.5)
print("Eva is good to go...")
speak("Eva is good to go...")
wishMe()

def commands():
    print("Command me master....")
    query = takeCommand()

    if 'wikipedia' in query.lower():
        speak('Searching wikipedia....')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        speak(result)

    elif "wake up" in query.lower():
        speak("Always here for you master...")
        print("Always here for you master")

    elif "hello" in query.lower():
        speak("Hello master, How can I help you...")
        print("Hello master, How can I help you")

    elif 'open youtube' in query.lower():
        speak("Opening YouTube...")
        webbrowser.get('windows-default').open("https://YouTube.com")

    elif "the time" in query.lower():
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"Master {MASTER} the time is {current_time}")
        print(current_time)

    elif "day" in query.lower():
        now = date.today()
        curr_date = date.today()
        week = calendar.day_name[curr_date.weekday()]
        speak(f"Master today's date is {now} and it's {week}...")
        print(f"Master today's date is {now} and it's {week}...")

    elif "date today" in query.lower():
        now = date.today()
        print(now)
        speak(f"Master today's date is {now}")

    elif "open spotify" in query.lower():
        speak("opening spotify...")
        click(x=1322, y=1055)

    elif "open code" in query.lower():
        code_path = "C:\\Users\\TARUN VEMULA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("opening vscode...")
        os.startfile(code_path)

    elif "open instagram" in query.lower():
        speak("opening instagram")
        webbrowser.get('windows-default').open("https://instagram.com")

    elif "open facebook" in query.lower():
        speak("opening facebook")
        webbrowser.get('windows-default').open("https://facebook.com")

    elif "open epic games" in query.lower():
        epic = "D:\\New folder\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"
        speak("opening epic games...")
        os.startfile(epic)

    elif "search for" in query.lower():
        speak("Searching Google....")
        query = query.replace("search google","")
        webbrowser.get('windows-default').open(f"https://www.google.com/search?q={query}")
        speak("Here's the result I got master....")

    elif "search youtube" in query.lower():
        speak("What should I search for master....")
        comm = takeCommand()
        speak("searching youtube....")
        webbrowser.get('windows-default').open(f"https://www.youtube.com/search?q={comm}")
        speak("Here's the result master....")

    elif "check instagram inbox" in query.lower():
        speak("Checking messages....")
        webbrowser.get('windows-default').open(f"https://www.instagram.com/direct/inbox/")

    elif "joke" in query:
        jokes = pyjokes.get_joke()
        speak(f"{jokes}....")
        print(jokes)

    elif "open whatsapp" in query.lower():
        speak("opening whatsapp...")
        click(x=1216, y=1059)

    elif "track" and "number" in query:
        speak("Please enter the number master....")
        mobileNo = input("Enter the required number with the country code : ")
        mobileNo = phonenumbers.parse(mobileNo)
        print(timezone.time_zones_for_number(mobileNo))
        speak(f"Master the region is {timezone.time_zones_for_number(mobileNo)}")
        print(carrier.name_for_number(mobileNo,"en"))
        speak("And the carrier is "+carrier.name_for_number(mobileNo,"en"))
        print(geocoder.description_for_number(mobileNo,"en"))
        speak("And the place is "+geocoder.description_for_number(mobileNo,"en"))
        print("Valid Mobile Number : ",phonenumbers.is_valid_number(mobileNo))
        print("Checking possibility of Number : ",phonenumbers.is_possible_number(mobileNo))

    elif "open teams" in query.lower():
        pt = "C:\\Users\\TARUN VEMULA\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
        speak("Opening microsoft teams....")
        os.startfile(pt)

    elif "open github" in query.lower():
        speak("opening github...")
        webbrowser.get('windows-default').open("https://www.github.com")

    elif "open chrome" in query.lower():
        speak("opening chrome")
        click(x=767, y=1061)

    elif "search spotify" in query.lower():
        speak("what song should I search for master....")
        song = takeCommand()
        speak(f"Searching for {song}....")
        click(x=1276, y=1061)
        time.sleep(15)
        click(x=63, y=120)
        time.sleep(3)
        click(x=676, y=41)
        time.sleep(1)
        write(f"{song}")
        press('enter')

    elif "who is your master" in query.lower():
        speak(f"My master name is {MASTER}....")
        speak("My master is born on april 10,2001....")

    elif "take rest" in query.lower():
        speak("sleeping...")
        time.sleep(50)
        speak("I'm awake master...")

    elif "thank you" in query.lower():
        speak("Always here to serve you master....")

    elif "exit" in query.lower():
        speak("On your command master...")
        speak("going offline...")
        exit()

    elif "go offline" in query.lower():
        speak("On your command master...")
        speak("going offline...")
        exit()

while True:
    commands()
while False:
    takeCommand()