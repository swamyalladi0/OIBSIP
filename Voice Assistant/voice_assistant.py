import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return ""

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak("Current time is " + time)

def tell_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + date)

def search_web(query):
    speak("Searching on Google")
    webbrowser.open("https://www.google.com/search?q=" + query)

def wiki_search(topic):
    result = wikipedia.summary(topic, sentences=2)
    speak(result)

speak("Hello, I am your Python Voice Assistant")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "search" in command:
        query = command.replace("search", "")
        search_web(query)

    elif "who is" in command:
        person = command.replace("who is", "")
        wiki_search(person)

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        break
