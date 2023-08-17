import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine=pyttsx3.init('sapi5')#microsoft api for voice recognition and synthesis
voices=engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice',voices[1].id)#to select the female voice of windows default(zara)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Gigi. How can I assist you")
    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1 #waiting time to end a sentence
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to,content):#will work only if you turn on less secure apps on google account
    # using smtplib
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourname@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    # speak("Amaan Zain N")
    wishMe()
    while True:
        query= takeCommand().lower()

        # logic is starting here

        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'open git' in query:
            webbrowser.open("https://github.com/amaanzain")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")

        elif 'play music' in query:
            music_dir='D:\\Music\\[SPOTIFY-DOWNLOADER.COM] New malayalam movie songs'
            songs=os.listdir(music_dir)
            print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))#to play music from start
            os.startfile(os.path.join(music_dir,songs[random.randint(0,26)]))#to play random music from the directory

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif "open movies" in query:
            mov_dir='D:\\movies'
            os.system(f'explorer "{mov_dir}"')

        elif "open series" in query:
            ser_dir='D:\\series'
            os.system(f'explorer "{ser_dir}"')

        elif "open music" in query:
            mus_dir='D:\\Music'
            os.system(f'explorer "{mus_dir}"')

        elif "open code" in query:
            code_path='c:\\Users\\zaina\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'#location of vs code here
            os.startfile(code_path)

        elif "email to zain" in query:
            try:
                speak("Tell me about the body of the mail...")
                content=takeCommand()
                to="zainamaanaz@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry!.. not able to send the mail right now")

        elif "exit" in query:
            print("exiting...")
            exit()
        
         
        






