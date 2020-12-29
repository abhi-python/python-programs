import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")

    else:
        speak("Good Evening!")  

    speak("hello! I am jarvis. Please tell me how may I help you!")      

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e) 
        print("Say that again please..")
        return "None" 
    return query  

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)   
    server.ehlo()
    server.starttls
    server.login("youremail@gmail.com", "yourpassword")     
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = take_command().lower() 
        # Logic for executing tasks based on query.
        if 'wikipedia' in query:
            speak ("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak ("According to wikipedia..")
            print(results)
            speak (results)
 
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)
            print (songs)        
            os.startfile(os.path.join(music_dir, songs[0]))   

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak (f"The time is {strtime}")    

        elif 'open code' in query:
            code_path = r"C:\\Users\\User\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(code_path)   

        elif 'email to abhi' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "youremail@gmail.com"
                sendemail = (to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend abhi! I am not able to send this email.")        