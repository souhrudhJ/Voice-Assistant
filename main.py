from speechToText import speech_input
from gemini import samantha
from textToSpeech import samantha_reply

text = speech_input()

if text:
    reply = samantha(text)
    print(f"Samantha: {reply}") 

    samantha_reply(reply)
else:
    print("No input detected")






