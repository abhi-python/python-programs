import requests
import json
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == "__main__":
    speak("News for today...Let's begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3d4d60d4deff47feb2273ef83af439c9"
    response = requests.get(url).text
    mydict = json.loads(response)
    print(mydict["articles"])
    arts = mydict['articles']
    for atricle in arts:
        speak(atricle['title'])   
        speak("Moving on to the next article...Listen carefully.")