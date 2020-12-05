# Simple AI Assistant made using Python. 
# Name = J.A.R.V.I.S; Just a Rather Very Intelligent System

#importing few python dependancies
from gtts import gTTS
import speech_recognition as sr
import os
import smtplib

#Saves the audio
def talk(audio):
    print(audio)
    tts =gTTS(text = audio, lang = 'en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listens
def my_Command():
    r = sr.Recognizer()
    with sr.Microphone () as source:
        print("I'm waiting for your next command")
        r.pause_threshhold = 1
        r.adjust_for_ambient_noise(source,duration = 1)  #This means that if you have any music or people talking in the background, JARVIS won't pick up that command and execute it 
        audio = r.listen(source)

    try: command = r.recognize_google(audio)
     # print('You have said:'+ command +'/n')

    #loop back to continue to listen to command
    # if JARVIS hears smthg in the background and doesn't understand it, 
    # this command will loop back 
    except sr.UnknownValueError:
        assistant(my_Command()) 
    return command 

# if and else statements for command execution
def assistant(command):
    if 'open mail' in command:
        chrome_path = 'https://www.google-chrome.com'
        url = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.get(chrome_path).open(url)
        talk('Opened Mail!')

    if 'what\'s up' in command:
        talk(" 'Nothing Much, Just chillin' ")    

    if 'open youtube' in command:
        chrome_path_two = 'https://www.google-chrome.com'
        url = 'https://youtube.com'
        webbrowser.get(chrome_path_two).open(url)
        talk('Opened Youtube! ')

talk('I am ready for your next command!')
while True:
    assistant(my_Command())