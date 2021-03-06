import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'senorita' in command:
                command = command.replace('senorita', '')
                # print("-->", command)
            else:
                print("Recall my name then talk!")
                talk("Recall my name then talk!")
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    # print("-->", command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)  # To give only 1 line informartion
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('Haha, Sorry I am in a relationship with Anuj')
    elif 'joke' in command:
        p = pyjokes.get_joke()
        print(p)
        talk(pyjokes.get_joke())
    elif command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)  # To give only 1 line informartion
        print(info)
        talk(info)
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
