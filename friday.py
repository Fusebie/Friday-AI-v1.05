import datetime
import pyttsx3
import os
import webbrowser
import wikipedia
import pywhatkit as kit
import random 
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

#speak(voices[0].id)

engine.setProperty('voice',voices[0].id)

# speak function 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# this will give the user a list of commands 
def help_user():
    print("-----List of commands---")
    print("                        ")
    print("the time (tells the user what the time is)")
    print("calculate (calculates the output of 2 numbers)")
    print("open whatsapp (opens whatsapp through browser)")
    print("open youtube (opens youtube)")
    print("open discord (opens discord through browser,can be modified)")
    print("open reddit (opens reddit)")
    print("open classroom (opens googleclassroom)")
    print("open gmail (opens gmail)")
    print("according to wikipedia(type 'according to wikipedia' next to what you want to want to search on wikipedia)")
    print("play music (plays music)")
    print("open chrome (opens chrome)")
    print("open vscode (opens vscode)")
    print("open telegram (opens telegram)")
    print("open unity hub (opens unity hub)")
    print("open unity (opens unity editor)")
    print("open bandicam (opens bandicam)")


# this will wish the user according current time
def wishme():

    print("                           ")
    print("---------Friday AI v1.03---------")
    print("-made by gourav,type help to get a list of commands")
    print("                           ")
    print("---what's new in 1.03--->")
    print("                           ")
    print("--> message [person's name] (opens whatsapp web and messages the specified person)")
    print("--> search google (searches google after topic is specified)")
    print("--> play youtube video (plays youtube video after title is specified)")
    print("                           ")
    print("                           ")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:

        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:

        print("Good Afternoon!")
        speak("Good Afternoon!")    
    else:

        print("Good Evening!")
        speak("Good Evening!")

    print("Hello I am Friday. Please tell me how may I help you")    

    speak("Hello I am Friday. Please tell me how may I help you")


# this will take input from user 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said: " + query)
        speak("user said: " + query)

    except Exception as e:
        print(e)
        print("say that again please...")
        speak("say that again please...")

        return "None"

    return query

# this currently only has text input. my pc is equivalent to a potato so i can't do voice input for now.

if __name__  == "__main__":

    loop_break_counter = 0

    wishme()

    while True:
        query = takecommand().lower()

        if 'open whatsapp' in query:
                speak("Opening whatsapp.")
                webbrowser.open("https://web.whatsapp.com")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + strtime)
            print("The time is " + strtime)

        elif '!say' in query:
            user_input = input("What do you want me to say? ")
            speak(user_input)
    
        elif 'calculate' in query:
            num1 = float(input("type the first number: "))
            op = input("type the operator: ")
            num2 = float(input("type the second number: "))

            resultLOL1 = 0

            if op == "+":
                resultLOL1 = num1 + num2

            elif op == "-":
                resultLOL1 = num1 - num2

            elif op == "*":
                resultLOL1 = num1 * num2

            elif op == "/":
                resultLOL1 = num1 / num2

            else:
                print("invalid operator")
                speak("invalid operator")

            print(resultLOL1)
            speak(resultLOL1)

        elif 'open youtube' in query:

            speak("Opening youtube")

            webbrowser.open('https://youtube.com')

        elif 'open discord' in query:
        
            speak("Opening discord")
            discordpath = "C:\\Users\\user\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe"
            os.startfile(discordpath)

        elif 'open classroom' in query:

            speak("Opening classroom")
            webbrowser.open('https://classroom.google.com/u/1/h')

        elif 'open reddit' in query:

            speak("Opening reddit")
            webbrowser.open("https://www.reddit.com/")

        elif 'open gmail' in query:

            speak("Opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'message sonam' in query:
            message_to_sonam = input("Type your message: ")
            kit.sendwhatmsg_instantly("+91 79809 72630",message_to_sonam,2)
            speak("Sending message to sonam..")
            print("Sending message to sonam..")

        elif 'message aditya' in query:
            message_to_adi = input("Type your message: ")
            kit.sendwhatmsg_instantly("+91 90885 91058", message_to_adi,2)
            speak("Sending Message to Aditya..")
            print("Sending Message to Aditya..")

        elif 'message anoush' in query: 
            message_to_anoush = input("Type your message: ")
            kit.sendwhatmsg_instantly("+91 98313 33457",message_to_anoush,2)
            speak("Sending Message to Anoush..")
            print("Sending Message to Anoush..")

        elif 'message manas' in query:
            message_to_manas = input("Type your message: ")
            kit.sendwhatmsg_instantly("+91 74397 27180",message_to_manas,)
            speak("Sending Message to Manas..")
            print("Sending Message to Manas..")

        elif 'message deep' in query:
            message_to_deep = input("Type your message: ")
            kit.sendwhatmsg_instantly("+91 79806 84690",message_to_deep,2)
            speak("Sending Message to Deep..")
            print("Sending Message to Deep..")

        elif 'message sagar' in query:
            message_to_sagar = input("Type your message: ")
            kit.sendwhatmsg_instantly("+91 82965 33310",message_to_sagar,2)
            speak("Sending Message to Sagar..")
            print("Sending Message to Sagar..")

        elif 'message aviraj' in query:
            message_to_aviraj = input("Type your message: ")
            kit.sendwhatmsg_instantly("+91 86480 90230", message_to_aviraj,2)
            speak("Sending Message to Aviraj..")
            print("Sending Message to Aviraj..")



        # elif 'message in bicchu gang' in query:
        #     message_to_bg = input("type your message: ")
        #     message_time_inHour = input("input the current time(hour): ")
        #     message_time_inMinutes = input("input the current time(minute): ")
        #     kit.sendwhatmsg_to_group("ItJUyr13cqW53b20VNN5kc",int(message_to_bg,message_time_inHour),int(message_time_inMinutes),3)

        elif 'play youtube video' in query:
            yt_vid_title = input("video title name: ")
            kit.playonyt(yt_vid_title)

        elif 'search google' in query:
            Google_search_topic = input("what do you want to search? ")
            kit.search(Google_search_topic)
            speak("Searching google...")
            print("Searching google...")

        # elif 'help pywhatkit' in query:
        #     kit.tutorial_english()

        elif 'open vscode' in query:

            speak("Opening Visual Studio Code...")
            vscodepath = "D:\\VS code\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)

        elif 'open spotify' in query:

            speak("Opening Spotify")
            musicpath = "C:\\Users\\user\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(musicpath)

        elif 'open chrome' in query:
            speak("Opening Chrome..")
            browserpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(browserpath)

        elif 'open telegram' in query:
            speak("Opening telegram...")
            tmPath = "D:\\Telegram Desktop\\Telegram.exe"
            os.startfile(tmPath)

        elif 'open unity hub' in query:
            speak("Opening Unity Hub...")
            UnityHubPath = "D:\\Unity hub\\Unity Hub.exe"
            os.startfile(UnityHubPath)

        elif 'open unity' in query:
            speak("Opening Unity Editor...")
            UnityEditorPath = "D:\\unity editor\\2020.3.19f1\\Editor\\Unity.exe"
            os.startfile(UnityEditorPath)

        elif 'open bandicam' in query:
            speak("Opening Bandicam Screen Recorder...")
            BandicamPath = "D:\\Bandicam\\bdcam.exe"

        elif query == "nothing":
            speak("okay...")

        elif query == "help":
            help_user()

        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'shutdown my computer' in query:
            
            shutdown_after_time = input("after(time): ")
            kit.shutdown(int(shutdown_after_time))
            print("Shutting down your computer...")
            speak("Shutting down your computer...")

        elif 'cancel shutdown' in query:

            kit.cancel_shutdown()
            print("Canceling shutdown...")
            speak("Canceling shutdown...")

        elif 'play music' in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            speak("Playing music...")
            os.startfile(os.path.join(music_dir, songs[random.randint(0,4)]))

        elif 'exit' in query:
            break

        else:
            print("command not recognized")
            speak("command not recognized")