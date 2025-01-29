import speech_recognition as sr
import pyaudio 

def speech_input():
    recognise = sr.Recognizer()

    with sr.Microphone() as source:
        print("speak now: ")
        audio = recognise.listen(source)

        try:    
            text = recognise.recognize_google(audio)
            print("you: {}".format(text))
            return text
        except:
            print("sorry, couldnt catch that")
            