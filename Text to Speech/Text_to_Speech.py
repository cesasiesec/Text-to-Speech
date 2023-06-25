##English Text to Speech
import pyttsx3

text = input("Enter text : ")

speech = pyttsx3.init()
speech.say(text)
speech.runAndWait()