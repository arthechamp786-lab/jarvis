import speech_recognition as sr
import webbrowser
import pyttsx3
import time

recognizer = sr.Recognizer()

def speak(text):
    print(f"Jarvis says: {text}")
    # Reinitialize engine each time to avoid driver conflicts
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening for wake word ('Jarvis')...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            try:
                word = recognizer.recognize_google(audio)
                print(f"Heard: {word}")
            except sr.UnknownValueError:
                print("Didn't catch that.")
                continue

            if "jarvis" in word.lower():
                speak("Yes?")
                print("Jarvis activated...")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.3)
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")

                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out — retrying...")
        except Exception as e:
            print(f"Error: {e}")

