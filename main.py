import speech_recognition as sr
import webbrowser
import pyttsx3
from musiclibrary import music
import requests
from google import genai
import subprocess
# pip install pocketsphinx

recognizer = sr.Recognizer()
newsapi= #get your own key
client = genai.Client()

def speak(text,rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate',rate)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[14].id)
    engine.say(text) 
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        ind= (c.lower().split(' ')).index('search')
        query='+'.join((c.lower()).split(' ')[ind+1:])
        if(query !=""):
            webbrowser.open(f"https://youtube.com/results?search_query={query}")
        else:
            webbrowser.open(f"https://youtube.com")
    elif "open linkedin" in c.lower():
         webbrowser.open("https://linkedin.com")
    elif "open chat gpt" in c.lower():
         webbrowser.open("https://chatgpt.com")
    elif ("gmail" in c.lower()) or ("mail" in c.lower()):
         webbrowser.open("https://gmail.com")
    elif("play" in c.lower()):
        song= (c.lower()).split(" ")[1]
        webbrowser.open(music[song])
    elif("news" in c.lower()):
        print('news running')
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        data=(r.json())["articles"]
        headlines=[article['title'] for article in data]
        for h in headlines:
            speak(str(h),200)
    elif("search" in c.lower()):
        formatted_query='+'.join((c.lower()).split(' ')[1:])
        google_search=f"https://www.google.com/search?q={formatted_query}"
        webbrowser.open(google_search)
    elif("open" in c.lower()):
        query=c.lower().split(' ')[1:]
        comm=' '.join([w.capitalize() for w in query])
        subprocess.call(['open', '-a', comm])
    elif("whatsapp" in c.lower()):
        subprocess.call(['open','-a',"WhatsApp"])
    elif("close" in c.lower()):
        query=c.lower().split(' ')[1:]
        comm=' '.join([w.capitalize() for w in query])
        subprocess.call(['killall', '-KILL', comm])
    elif("whatsapp" in c.lower()):
        subprocess.call(['killall','-KILL',"WhatsApp"])
        

    else:
        response = client.models.generate_content(model="gemini-2.5-flash", contents=c.lower()+".Give short and brief response")
        speak(response.text)
        
if __name__=="__main__":

    speak("Initializing Jarvis...")

    #Listen for the wake word Jarvis
    while (True):
        r = sr.Recognizer()

        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source,timeout=5)
            query= r.recognize_google(audio)   
            print("Jarvis listened " + query)
            print(query.lower())

            if (("thank you" in query.lower()) or ("thank" in query.lower())):
                speak("Welcome, Have a great day")
                break
            elif(("quit") in query.lower()) or ("exit" in query.lower()):
                speak("Goodbye, Have a nice Day!")
                break
            elif("jarvis" in query.lower()):
                speak("Ya")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio= r.listen(source,timeout=6)
                    command= r.recognize_google(audio)
                    processCommand(command)
            
        except Exception as e:
            print("Error,{}".format(e))
