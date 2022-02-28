 from tkinter import *
 import speech_recognition as sr
 import pyttsx3
 from datetime import datetime
 
 
 root=Tk()
 root.geometry=("500x500")
 
 
 text_to_speech=pyttsx3.init()
 
 def speak(audio):
     text_to_speech.say(audio)
     text_to_speech.runAndWait()
 
 def r_audio():
     speak("How can I help you..?")
     speech_recognisor = sr.Recognizer()
     with sr.Micrphone as source: 
         audio = speech_recognisor.listen(source)
         voice_data=''
         
         try:
             voice_data=speech_recognisor.recognize_google(audio, language='en-in')
             
         except sr.UnknownValueError:
             print("I did not get that in my voice list")
             speak("Please repeat i did not get that")
    
    def respond(voice_data)
        voice_data = voice_data.lower()
        print(voice_data)
        
        if "name" in voice_data:
            speak("My name is Jarvis")
            
            
        if "time" in voice_data:
            speak("Current time is")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            speak(current_Time)
        
 r_audio()
 root.mainloop()