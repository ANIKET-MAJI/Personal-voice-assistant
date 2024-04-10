import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recordedaudio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print('Your message:', format(text))

    except Exception as ex:
        print(ex)
        
    # Add auto-reply functionality
    if 'hello senpai' in text:
        e = 'Hello Sir, Welcome Back!'
        engine.say(e)
        engine.runAndWait()
        
    # Add auto-reply functionality
    if 'your name' in text:
        e = 'my name is Senpai, how can I help you sir!'
        engine.say(e)
        engine.runAndWait()  

    # Add auto-reply functionality    
    if 'work' in text:
        e = 'I am here to help, what can i do for you?'
        engine.say(e)
        engine.runAndWait()
    
    # Add auto-reply functionality
    if 'how are you' in text:
        reply = "I'm fine, thanks for asking!"
        engine.say(reply)
        engine.runAndWait()

    # Add auto-reply functionality
    if 'tell me a joke' in text:
        e = "Why don't some couples go to the gym?...Because some relationships don't work out"
        engine.say(e)
        engine.runAndWait()
    
    # Add auto-reply functionality
    if 'another joke' in text:
        e = 'What is the most shocking city in the world?...Electricity'
        engine.say(e)
        engine.runAndWait()

    # Add auto-reply functionality
    if 'about you' in text:
        e = 'i am senpai, i am your personal voice assistant, created by Subrata Maji,...Amiket Maji,...Subrata Roy,...Ayush kumar sharma'
        engine.say(e)
        engine.runAndWait()   

    if 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        engine.say(current_time)
        engine.runAndWait()

    if 'chrome' in text:
        a = 'Opening chrome...'
        engine.say(a)
        engine.runAndWait()
        programName = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
    
    if 'play' in text:
        a = 'Opening youtube...'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
        
    if 'youtube' in text:
        b = 'Opening youtube...'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
        
    if 'open notepad' in text:
        c = 'Opening notepad...'
        engine.say(c)
        engine.runAndWait()
        webbrowser.open('c:\\windows\\system32\\notepad.exe')
        
    elif 'close notepad' in text:
        c = 'Closing notepad...'
        engine.say(c)
        engine.runAndWait()
        os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')

    if 'open mail' in text:
        d = 'Here you go to mail\n'
        engine.say(d)
        engine.runAndWait()
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
      
while True:
    cmd()
