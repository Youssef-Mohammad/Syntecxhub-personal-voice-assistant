# Import necessary libraries
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pywhatkit
import wikipedia
import time

# -------------------------------------
# Global Speech Settings
# -------------------------------------

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.3
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

mic = sr.Microphone()

WAKE_WORD = "alexa"

# -------------------------------------
# Text-to-Speech
# -------------------------------------

def speak(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 175)
    voice_id = engine.getProperty('voices')[1].id
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# -------------------------------------
# Wake Word Listener
# -------------------------------------

def listen_for_wake_word():
    with mic as source:
        print("🛑 Idle — waiting for wake word...")

        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio).lower()
            print("Heard:", text)

            return WAKE_WORD in text

        except sr.UnknownValueError:
            return False
        except sr.RequestError:
            return False

# -------------------------------------
# Command Listener
# -------------------------------------

def listen_for_command():
    with mic as source:
        print("🎧 Listening for command...")

        try:
            audio = recognizer.listen(
                source,
                timeout=5
            )
        except sr.WaitTimeoutError:
            return None

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return None

# -------------------------------------
# Command Processing
# -------------------------------------

def process_command(command):

    if "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "play" in command and "playlist" not in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        speak(f"Playing {song}")

    elif "search" in command:
        query = command.replace("search", "")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")

    elif "who is" in command:
        person = command.replace("who is", "")
        try:
            info = wikipedia.summary(person, sentences=2)
            speak(info)
        except:
            speak("I couldn't find information about that")

    elif "playlist" in command:
        speak("Playing your playlist")
        playlist_path = r"D:\Songs\my_playlist.m3u"
        os.startfile(playlist_path)

    elif "nothing" in command or "cancel" in command:
        speak("Okay, cancelled")

    elif "bye" in command or "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Sorry, I don't understand that command.")

# -------------------------------------
# Main Assistant Logic
# -------------------------------------

def run_assistant():

    speak("Assistant started. Say Alexa to wake me.")

    # Calibrate once at startup
    with mic as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:

        if listen_for_wake_word():

            speak("Yes?")
            time.sleep(0.2)  # prevents mic transition freeze

            command = listen_for_command()

            if command:
                print("Command:", command)
                process_command(command)
            else:
                speak("I didn't hear a command.")

run_assistant()