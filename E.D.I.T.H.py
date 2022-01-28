import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Creating a voice for the AI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Setting the voice to male or female
engine.setProperty('voice', voices[1].id)

stop = False

# Function to allow the AI to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Greeting based on the time of day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am EDITH sir. Please tell me how may I help you.")

# Takes audio from microphone and saves it as the query
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def createList():
    done = False
    number = 1
    textlist = []

    speak("Say finished when the list is over.")
    while not done:
        speak("Tell me what is number" + str(number) + "on your list")
        todo = takeCommand()
        if 'None' not in todo:
            number = number + 1
            if 'finished' in todo:
                done = True
            else:
                textlist.append(todo)

        else:
            speak("I didn't hear that, please say it again")
    toDoFile = open("To Do List.txt", "w+")
    toDoFile.write("        To Do List\n")
    for i in range(len(textlist)):
        toDoFile.write(str(i+1) + ". " + textlist[i] + "\n")
    filePath = "C:\\Users\\red20\\OneDrive\\Desktop\\Github Projects\\Software\\E.D.I.T.H\\To Do List.txt"
    os.startfile(filePath)

def readList():
    print("")
        #Put items in list
    #Take out periods from List
    #REad out list

if __name__ == '__main__':
    wishMe()
    while not stop:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'thank you' in query:
            speak("Your Welcome")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.ca")

        elif 'open discord' in query:
            discordPath = "C:\\Users\\red20\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe"
            os.startfile(discordPath)

        elif 'stop listening' in query:
            speak("Good Bye")
            stop = True

        elif 'create a to-do list' in query:
            createList()
            speak("Your to-do list has been created. Do you require anything else?")

        elif 'read my to-do list' in query:
            readList()
