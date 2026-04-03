import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        speak("Sorry, I didn't understand.")
        return ""

def run_assistant():
    speak("Hello! How can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello there!")

        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time_now}")

        elif "date" in command:
            date_today = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date_today}")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "your name" in command:
            speak("I am your voice assistant")

        elif "search" in command:
            query = command.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("I can only do basic tasks right now.")

run_assistant()
