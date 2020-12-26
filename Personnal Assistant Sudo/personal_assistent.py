import pyttsx3  #pip install pyttsx3
import datetime  #module
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os  #inbuilt
import pyautogui
import psutil  #pip install psutil
import pyjokes  # pip install pyjokes
import requests, json  #inbuilt
from covid19_data import JHU
# import wolframalpha

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)


#change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    print("Sudo: Done sir")
    speak("Done sir")


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Sudo: The current time is "+ Time)
    speak("The current time is "+ Time)
    


#covid function
def covid_19():
    # print("Sudo: tell me which country")
    # speak("tell me which country")
    # country_name = takeCommand()
    print("Sudo: here's the details")
    speak("here's the details")
    print("The total number of COVID-19 cases in India: ", str(JHU.India.confirmed))
    speak("The total number of COVID-19 cases in India: " + str(JHU.India.confirmed))
    print("The total number of COVID-19 deaths in India: " + str(JHU.India.deaths))
    speak("The total number of COVID-19 deaths in India: " + str(JHU.India.deaths))
    print("The total number of COVID-19 recoveries in India: " + str(JHU.India.recovered))
    speak("The total number of COVID-19 recoveries in India: " + str(JHU.India.recovered))
    print("Sudo: And the interesting thing is that, Rohan You are one of the recovered patient!\nHope you well now!")
    speak("And the interesting thing is that, Rohan You are one of the recovered patient!\nHope you well now!")

    # print("The number of worldwide COVID-19 deaths: " + str(JHU.Total.deaths))
    # print("The number of worldwide COVID-19 confimed cases: " + str(JHU.Total.confirmed))
    # print("The number of worldwide Conid-19 recovered patients: " + str(JHU.Total.recovered))
#date function
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print("Sudo: The current date is " + f"{date}-{month}-{year}")
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


#welcome function
def wishme():
    print("Sudo: Welcome Back")
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        print("Good Morning Rohan!")
        speak("Good Morning Rohan!")
    elif (hour >= 12 and hour < 18):
        print("Good afternoon Rohan!")
        speak("Good afternoon Rohan")
    elif (hour >= 18 and hour < 24):
        print("Good evening Rohan!")
        speak("Good Evening Rohan")
    else:
        print("Goodnight Rohan!")
        speak("Goodnight Rohan")
        
    print("Sudo at your service, Please tell me how can i help you?")
    speak("Sudo at your service, Please tell me how can i help you?")


def wishme_end():
    print("Sudo: I am glad i could help you, I am going to offline now, See you soon BYE!")
    speak("I am glad i could help you, I am going to offline now, See you soon BYE!")
    quit()


#command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sudo: Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Sudo: Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #speak(query)
        print("You: " + query + "?")
    except Exception as e:
        print(e)
        print("Sudo: Say that again please...")
        speak("Say that again please...")

        return "None"

    return query


#sending email function
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("user-name@xyz.com", "pwd")
    server.sendmail("user-name@xyz.com", to, content)
    server.close()


#screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\ss.png")

# def wol():
    # app_id = "HQ7T69-ELPTL94PXH"
    # client = wolframalpha.Client(app_id)
    # query = takeCommand()
    # res = client.query(query)
    # answer = next(res.results).text
    # print(answer) 
    # speak(answer)


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('Sudo: CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("Sudo: battery is at:" + str(battery.percent))


#joke function
def jokes():
    j = pyjokes.get_joke()
    print("Sudo: "+j)
    speak(j)


#weather condition
def weather():
    api_key = "7cf25c285049def3cf10a131836a3343" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    print("Sudo: tell me which city")
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak("Sudo: City Not Found ")


def personal():
    print("I am Sudo, version 1.0, I am your personal AI assistent,\nI am developed by Rohan on 06 november 2020 in Gwalior India")
    speak("I am Sudo, version 1.0, I am your personal AI assistent,\nI am developed by Rohan on 06 november 2020 in Gwalior India")
    print("Sudo: Now i hope you know me")
    speak("Now i hope you know me")
    



if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

#time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()
            
#covid
        elif ("covid details" in query or "covid details of india" in query or "tell me covid-19 detail" in query or "tell me Covid-19 details" in query or "covid-19 details" in query or "tell me covid details" in query or "tell me covid details of india" in query or "can you tell me covid details of india" in query or "can you tell me covid details" in query or "can you tell me Covid-19 details of india" in query or 'Can you tell me Covid-19 details' in query):
            covid_19()
            

#personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        elif ("developer" in query or "tell me about your developer" in query or "father" in query 
        or "who develop you" in query or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

#searching on wikipedia

        elif ('wikipedia search' in query or 'wikipedia' in query or 'search' in query 
        or 'what' in query or 'who' in query or 'who is' in query or 'what is' in query 
        or 'when' in query or 'where' in query or "who is the" in query or "tell me about" in query):
            try:             
                print("searching...")
                query = query.replace("wikipedia", "")
                query = query.replace("wikipedia search", "")
                query = query.replace("tell me about", "")
                query = query.replace("search", "")
                query = query.replace("what", "")
                query = query.replace("what is", "")
                query = query.replace("when", "")
                query = query.replace("where", "")
                query = query.replace("who", "")
                query = query.replace("who is", "")
                query = query.replace("who is the", "")
                query = query.replace("is", "")
                print("Sudo: "+result)
                speak(result)
            except Exception as e:
                print(e)
                print("Sudo: Sorry, I am Unable to search" + query)
                speak("Sorry, I am Unable to search" + query)

#sending email

        elif ("send email" in query):
            try:
                print("Sudo: What is the message for the email")
                speak("What is the message for the email")
                content = takeCommand()
                to = 'reciever@xyz.com'
                sendEmail(to, content)
                print("Email has sent")
                speak("Email has sent")
            except Exception as e:
                print(e)
                print("Sudo: Unable to send email check the address of the recipient")
                speak("Unable to send email check the address of the recipient")
                
        elif ("search on google" in query or "open website" in query or "can you do google search" in query or "can you do google search for me" in query
        or "can you search on google" in query or "google search" in query or "can you search for me" in query 
        or "can you open something" in query or "can you open google" in query or "open google" in query):
            print("Sudo: What should i search or open?")
            speak("What should i search or open?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
            print("Sudo: searching...")
            break
        
        elif ('open youtube' in query or "can you open youtube" in query
        or "can you open youtube for me" in query or "please open youtube" in query or "youtube" in query):
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab("youtube.com")
            print("youtube is opened")
            speak("youtube is opened")
            
        elif ('open facebook' in query or "can you open facebook" in query
        or "can you open facebook for me" in query or "please open facebook" in query or "facebook" in query):
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chromepath).open_new_tab("facebook.com")
            print("youtube is opened")
            speak("youtube is opened")

#sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

#play songs

        elif ("play songs" in query or "can you play songs" in query or "play music" in query or "gana sunayen" in query or "gaana sunayen" in query or "can you open music for me" in query):
            print("Sudo: playing...")
            speak("Playing...")
            songs_dir = "H:\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[41]))
            quit()
            

#reminder function

        elif ("create a reminder list" in query or "reminder" in query or "set reminder" in query):
            print("Sudo: What is the reminder?")
            speak("What is the reminder?")
            data = takeCommand()
            print("You said to remember that" + data)
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            print("Sudo: You said me to remember that: " + reminder_file.read())
            speak("You said me to remember that: " + reminder_file.read())

#screenshot
        elif ("screenshot" in query or "take screenshot" in query or "take screenshot now" in query):
            screenshot()
            print("Sudo: Done and Saved!")
            speak("Done and Saved!")

#cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query or "cpu" in query or "battery usage" in query or "cpu usage" in query):
            cpu()

#jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#weather
        elif ("weather" in query or "temperature" in query or "tell me weather details" in query or "weather info" in query):
            weather()

#jarvis features
        elif ("tell me about you " in query or "help" in query
              or "features" in query or "what you can do?" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print("Sudo :"+ features)
            speak(features)

        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("sudo", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                print("Sudo: what can i do for you")
                speak("what can i do for you")

#changing voice
        elif ("voice" in query or "change voice" in query or "change your voice" in query):
            print("Sudo: for female say female and, for male say male")
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q or "mail" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

#exit function

        elif ('i am done' in query or 'bye bye jarvis' in query
              or 'go offline sudo' in query or 'bye' in query
              or 'nothing' in query or "OK bye" in query or "ok thank you" in query or "thank you" in query or "Stop" in query or "Close" in query):
            wishme_end()