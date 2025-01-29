from gtts import gTTS
import os 
from playsound import playsound




def samantha_reply(text):
    output = gTTS(text=text, lang='en', slow=False)
    output.save("tts.mp3")

    playsound("tts.mp3")

    os.remove("tts.mp3")