
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyautogui
import time

listener = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<12:
        talk(f'good morning , its {tt}')

    elif hour>=12 and hour<18:
        talk(f'good afternoon ,its {tt}')

    else:
        talk(f'good evening ,its {tt}')
    talk('  how may i help you .. ')

def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening ...')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday','')
                print(f'user said :',command)
    except:
        pass
    return command

def run_friday():
    WishMe()
    while True:
        command = take_command()
        print(command)

        if 'play' in command:
            song = command.replace('play','')
            talk('playing' + song)
            pywhatkit.playonyt(song)


        elif 'time' in command:
            tm = time.strftime("%I %M %p")
            talk('the current time is' + tm)
            print(tm)

        elif 'wikipedia' in command:
            person = command.replace('wikipedia','')
            info = wikipedia.summary(person,1)
            print(info)
            talk(info)

        elif 'shut up' in command:
            talk('no you shut up , dont try to act smart')

        elif 'thank you ' in command:
            talk('your welcome sir, always here at your service')

        elif 'are you single' in command:
            talk(' o no ,i am in a relationship with wifi')

        elif 'how are you' in command:
            talk('i am good ,sir , how are you')

        elif 'hello' in command:
            talk('hello sir ,good to see you')



        elif 'working' in command:
            talk('currently i am working for sir jabez')

        elif  'search on google' in command:
            search = command.replace('search on google','')
            talk('searching' + search)
            pywhatkit.search(search)

        elif 'open whatsapp' in command:
            webbrowser.open('https://web.whatsapp.com')
            talk('almost there')

        elif 'open youtube' in command:
            webbrowser.open('https://www.youtube.com')
            talk('already on it sir')

        elif ' open google' in command:
            webbrowser.open('https://www.google.com')
            talk('opening google')

        elif 'open browser' in command:
            apppath = "C:\\Users\\jabez\\AppData\\Local\\Programs\\Opera GX\\opera.exe"
            os.startfile(apppath)
            talk('opening browser')

        elif 'close browser' in command:
            talk('on it sir, closing browser')
            print('closing browser')
            os.system('taskkill /f /im opera.exe')

        elif 'open VScode' in command:
            codePath = "C:\\Users\\jabez\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            talk('opening VScode')

        elif 'close VScode' in command:
            talk('on it sir,closing VScode')
            print('closing VScode')
            os.system('taskkill /f /im Code.exe')


        elif 'about you' in command:
            talk('i am friday,an assistant built to reduce your efforts by doing some simple tasks , created by sir jabez on 18th january 2022,at 12 46 am')

        elif 'open instagram' in command:
            webbrowser.open('https://www.instagram.com/?hl=en')
            talk('almost there')


        elif 'discord' in command:
            webbrowser.open('https://discord.com/channels/@me')
            talk('on my way into  discord')


        elif 'open notepad' in command:
            nt = "C:\\Windows\\System32\\notepad.exe"
            print('opening notepad')
            os.startfile(nt)
            talk('opening notepad')

        elif 'close notepad' in command:
            talk('closing notepad')
            os.system("taskkill /f /im notepad.exe")


        elif 'spider-man' in command:
            talk('no not yet , i dont have enough money to buy the tickets')

        elif 'no thanks' in command:
            talk('i will be away for a while , wake me up if you need anything')
            print('i will be away for a while , wake me up if you need anything')
            break

        elif 'volume up' in command:
            pyautogui.press('volumeup')

        elif 'volume down' in command:
            pyautogui.press('volumedown')

        elif 'volume mute' in command  or 'mute' in command:
            pyautogui.press('volumemute')

        elif 'google search' in command:
                command = command.replace('google search','')
                talk('this is what i found on the web')
        try:
                pywhatkit.search(command)
                result = wikipedia.summary(command,2)
                talk(result)
        except:
                 talk('no speakable data available on this google search')

        else:
            talk('dint get you sir ')

            talk('anything else sir')

while True:
    global per
    per = take_command()
    if 'wake up ' in per:
        talk('welcome back sir ,.....we are connected and ready to go')
        run_friday()

    elif 'quit' in per:
        talk('thank you for giving me your time, have a great day ahead')
        sys.exit()
