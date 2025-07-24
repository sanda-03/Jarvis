import webbrowser
import speech_recognition as sr
def search(c):
    formatted_query='+'.join((c.lower()).split(' ')[1:])
    google_search=f"https://www.google.com/search?q={formatted_query}"
    webbrowser.open(google_search)

with sr.Microphone() as source:
    print("Say something!")
    r=sr.Recognizer()
    audio = r.listen(source,timeout=5)
    query= r.recognize_google(audio)   
    print("Jarvis listened " + query)
    search(query)