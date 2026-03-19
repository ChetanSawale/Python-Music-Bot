import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyautogui
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

run = True

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():

    global run

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print("User:", text)

            if "chetan" not in text:
                return

            command = text.replace("chetan", "").strip()

            if "exit" in command:
                speak("Goodbye")
                run = False
                return

            if "play" in command:

                song = command.replace("play", "").strip()

                speak(f"Playing {song}")

                time.sleep(0.5)

                pywhatkit.playonyt(song)

            elif "pause" in command:
                speak("Pausing music")
                time.sleep(1)
                pyautogui.press("space")

            elif "resume" in command:
                speak("Resuming music")
                time.sleep(1)
                pyautogui.press("space")

            elif "next" in command:
                speak("Playing next song")
                time.sleep(1)
                pyautogui.hotkey("shift", "n")

        except sr.UnknownValueError:
            print("Could not understand")

while run:
    listen()