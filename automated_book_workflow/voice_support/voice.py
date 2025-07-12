import speech_recognition as sr
import pyttsx3

def voice_output(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voice_prompt():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("User said:", text)
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""
