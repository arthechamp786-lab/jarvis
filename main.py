import speech_recognition as sr
import webbrowser
import pyttsx3 
import musicLibrary
import alakhMemes
import requests
from google import genai



recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi = "6bb38066a5214e25a5684691a0b2790b"

def speak(text):
    engine=pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()
    
def ask_genai(command):
    
    client = genai.Client(api_key="AIzaSyCYVZWxSFZx1MZPG6d20EXSQWaSAHFfD90")
                


    response = client.models.generate_content(
       model="gemini-2.5-flash", contents=command
       )
    return response.text

    
    
def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        speak("opening instagram")
        webbrowser.open("https://www.instagram.com")
        
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1 ]
        link=musicLibrary.music[song]
        webbrowser.open(link)
        
    elif c.lower().startswith("show"):
        meme=c.lower().split(" ")[1]
        url=alakhMemes.alakh[meme]
        webbrowser.open(url)
    
    elif "news" in  c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?sources=the-times-of-india,the-hindu,google-news-in&apiKey={newsapi}")
        
        if r.status_code == 200:
            #parse the json response
            data=r.json()
            #Extract the articles
            articles = data.get('articles',[])
            #print the articles
            for article in articles:
                speak(article['title'])
    else:
        output=ask_genai(c)
        speak(output)
        
        
if __name__ == "__main__":
    speak("initiallizing Jarvis")
    
    while True:
    #Listen for the wake word("jarvis")
    # obtain audio from the microphone
    # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
            word=r.recognize_google(audio)
            
            if "jarvis" in word.lower():
                speak("jarvis activated")
                print("Jarvis activated...")
                

                with sr.Microphone() as source:
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    
                processCommand(command)
                    
        
        except Exception as e:
            print("error; {0}".format(e))