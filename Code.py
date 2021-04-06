import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ =='__main__':
    z=1
    speak("Todays news are")
    url="https://newsapi.org/v2/everything?q=tesla&from=2021-03-06&sortBy=publishedAt&apiKey=925cab3aaa9d42799eb03bcfc641e3e7"
    news=requests.get(url).text
    news_d=json.loads(news)
    art=news_d['articles']
    for i in art:

        speak(f"news number {z} is")
        speak(i['title'])
        z+=1
