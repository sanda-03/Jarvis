import webbrowser
import speech_recognition as sr
def search(c):
    query=c.lower().split(' ')[1:]
    comm=' '.join([w.capitalize() for w in query])
    print(comm)

with sr.Microphone() as source:
    print("Say something!")
    r=sr.Recognizer()
    audio = r.listen(source,timeout=5)
    query= r.recognize_google(audio)   
    print("Jarvis listened " + query)
    search(query)
