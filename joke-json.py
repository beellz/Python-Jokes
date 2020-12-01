from urllib import request 
import json
import pyttsx3


engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate


voices = engine.getProperty('voices') 
voices = engine.setProperty('voice', voices[1].id)

URL = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(URL)
# print(r.getcode())
data = r.read()
jsondata = json.loads(data)
# print(jsondata)

class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"setup: {self.setup} punchline: {self.punchline}"

jokes = []

for j in jsondata:
    setup = j["setup"]
    punchline = j["punchline"] 
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f" got {len(jokes)} jokes")

for joke in jokes:
    print(joke)
    pyttsx3.speak("setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("the punchline")
    pyttsx3.speak(joke.punchline)


# print(r.read())
# pyttsx3.speak("setup")
# pyttsx3.speak(joke.setup)
# pyttsx3.speak("the punchline")
# pyttsx3.speak(joke.punchline)
