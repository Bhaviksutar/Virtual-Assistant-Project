
import speech_recognition as sr    #To convert speech into text
import pyttsx3                     #To convert text into speech
import datetime                    #To get the date and time
import wikipedia                   #To get information from wikipedia
import webbrowser                  #To open websites
import os                          #To open files
import time                        #To calculate time
import subprocess                  #To open files
import PyDictionary as PyDictionary
import pyautogui
import sys 
import pywhatkit as kt
import smtplib
from email.message import EmailMessage
from tkinter import *              #For the graphics
import pyjokes                     #For some really bad jokes
from playsound import playsound    #To playsound
import keyboard                    #To get keyboard
  
name_file = open("Assistant_name", "r")
name_assistant = name_file.read()




#DICTIONARY OF MAILS
mailDict ={
    "dhananjay":"dhananjaych0806@gmail.com",
    "bhavik":"bhaviksutar352002@gmail.com",
    "Chinya":"chinmaychavan07@gmail.com",
    "DC":"2019016401596644@mdcollege.in"}

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)



#global screen
screen = Tk()


global var
global var1

var = StringVar()
var1 = StringVar()

    
def speak(text):
    engine.say(text)
    print(name_assistant + " : "  +  text)
    engine.runAndWait() 


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        var.set("Good morning sir")
        screen.update()
        speak("Good morning sir")

    elif hour>=12 and hour<18:
        var.set("Good afternoon sir")
        screen.update()
        speak("Good afternoon sir")
    
    else:
        var.set("Good evening sir")
        screen.update()
        speak("Good evening sir")
    speak("i am mee,   how can i help you sir!")




def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening....")
        screen.update()
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold=4000
        r.phrase_threshold = 0.8
        audio = r.listen(source)

    try:
        var.set("Recognizing....")
        screen.update()
        print("Recognizing....")
        query = r.recognize_google(audio, language ='en-in')
        #if 'me' in query:
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        var.set("Say that again please...")
        screen.update()
        print("Say that again please...")
        #speak("Say that again please...")
        return "None"
    var1.set(query)
    screen.update()
    return query.lower()

            

def note():
    var.set("what you want to write sir")
    screen.update()
    speak("what you want to write sir")
    write = takeCommand()
    #date =datetime.datetime.now().strftime("%H:%M:%S")
    file_name = takeCommand() + "-note.txt"

    with open(file_name, "w") as f:
        f.write(write)

    path_1 ="D:\\virtual assistant final file\\"+str(file_name)
    path_2 ="D:\\virtual assistant final file\\database\\notepad files\\"+str(file_name)

    os.rename(path_1,path_2)
    os.startfile(path_2)

    subprocess.Popen(["notepad.exe", file_name])
    var.set("notepad file saved")
    screen.update()
    speak("notepad file saved")



def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 
    var.set("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')
    screen.update()
    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')

#EMAIL DEF FUNCTION
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('virtualbotmee@gmail.com','iambot@0806')
    email =EmailMessage()
    email['From'] ='virtualbotmee@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
    server.close()

def markattendance(query):
    with open('history.csv','r+') as f:
        f.readlines()
    time =datetime.datetime.now().strftime(" Hours:%H minutes:%M ")
    f = open('history.csv','a+')
    f.write(query  )
    f.write(time )
    f.write('\n')
    f.close()




def TaskExecution():
    global speak
    wishMe()

    
    while True:
        query = takeCommand().lower()
        markattendance(query)
        
       
        
        if 'wikipedia' in query:
            try:
                var.set('searching wikipedia...')
                screen.update()
                speak('searching wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                print(results)
                speak("According to wikipeadia ")
                var.set(results)
                screen.update()
                speak(results)

            except Exception as e:
                var.set("sorry sir, I am not able to find")
                screen.update()
                speak("sorry sir, I am not able to find")


        elif'on youtube'in query:
            song = query.replace('play','')
            var.set('playing'+ song)
            screen.update()
            speak('playing'+ song)
            kt.playonyt(song)

    

        elif'on google'in query:
            var.set("ok sir, searching on google")
            screen.update()
            speak("ok sir, searching on google")
            query=query.replace("mee","")
            query=query.replace("on google search","")
            kt.search(query)
            var.set("this is what i found for your search sir!!")
            screen.update()
            speak("this is what i found for your search sir!!")

        elif 'website' in query:
            var.set("opening...")
            screen.update()
            speak("opening...")
            #name = takeCommand()
            query=query.replace("mee","")
            query=query.replace("website","")
            query=query.replace("open","")
            webbrowser.open( 'google.com'+ query +".com" )
            speak("here is your result")

        elif'the time'in query:
            time =datetime.datetime.now().strftime("%H'Hours':%M 'minutes':%S 'seconds'")
            print(time)
            var.set(f"sir, the time is{time}")
            screen.update()
            speak(f"sir, the time is{time}")

        elif'open vs code' in query:
            var.set('Opening vs code')
            screen.update()
            speak('Opening vs code')
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'map' in query:
            query = query.replace('search',"")
            query = query.replace('on map',"")
            var.set("okay sir searching for" + query)
            screen.update()
            speak("okay sir searching for" + query)
            speak('')
            webbrowser.open("https://www.google.com/maps/place/" + query)


# CLOSING FUNCTIONS
        elif'close vs code' in query:
            var.set('closing vs code')
            screen.update()
            speak('closing vs code')
            os.system("TASKKILL /F /im Code.exe")

        elif'close youtube' in query:
            var.set("closing youtube sir!!")
            screen.update()
            speak("closing youtube sir!!")
            os.system("TASKKILL /F /im chrome.exe")
        
        elif'close google' in query:
            var.set("closing google sir!!")
            screen.update()
            speak("closing google sir!!")
            os.system("TASKKILL /F /im chrome.exe")
        
        elif'close wikipedia' in query:
            var.set("closing wikipedia sir!!")
            screen.update()
            speak("closing wikipedia sir!!")
            os.system("TASKKILL /F /im chrome.exe")

# EMAIL FUNCTION      
        elif 'send email' in query:
            try:
                var.set("To whom you want to send email")
                screen.update()
                speak("To whom you want to send email")
                name=takeCommand()
                receiver = mailDict[name]
                var.set("what is the subject of the mail")
                screen.update()
                speak("what is the subject of the mail")
                subject = takeCommand()
                var.set("what is the message or text of the mail")
                screen.update()
                speak("what is the message or text of the mail")
                message = takeCommand()
                send_email(receiver, subject, message)
                var.set("Email has been sent!")
                screen.update()
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                var.set("sorry sir, I am not able to send this email")
                screen.update()
                speak("sorry sir, I am not able to send this email")

# JOKE FUNCTION
        elif 'joke' in query:
            var.set(pyjokes.get_joke())
            screen.update()
            speak(pyjokes.get_joke())

# ASSISTANT CLOSE FUNCTION
        elif 'goodbye me' in query:
            var.set('ok sir!! goodbye')
            screen.update()
            speak('ok sir!! goodbye')
            sys.exit()

        elif 'take a break' in query:
            var.set("ok sir, you can call me any time")
            screen.update()
            speak("ok sir, you can call me any time")
            break
# SYSYTEM RESTART FUNCTION
        elif 'restart pc' in query:
            var.set("Do you want to restart")
            screen.update()
            speak("Do you want to restart")
            query= takeCommand()
            if 'yes' in query:
                var.set("system is restarting")
                screen.update()
                speak("system is restarting")
                os.system('shutdown /r /t 0')
            else:
                var.set("sorry sir,I am not able to hear any response about restar pc ")
                screen.update()
                speak("sorry sir,I am not able to hear any response about restar pc ")
# BASIC FUNCTIONS
        elif "hello" in query:
            var.set("Hello sir, i am mee your assistant   how may i help you")
            screen.update()
            speak("Hello sir, i am mee your assistant   how may i help you")

        elif 'how are you' in query:
            var.set("i am fine sir")
            screen.update()
            speak("i am fine sir")
            var.set("what about you")
            screen.update()
            speak("what about you")

            about = takeCommand()
            if "fine" in about:
                var.set("it is great sir i am glad to hear that")
                screen.update()
                speak("it is great sir i am glad to hear that")
            elif "good" in about:
                var.set("it is great sir i wish you have a great day ahead")
                screen.update()
                speak("it is great sir i wish you have a great day ahead")
            elif "not well" in about:
                var.set("what happend sir is that everything is fine")
                screen.update()
                speak("what happend sir is that everything is fine")
                query=takeCommand()
                if "lost" in query:
                    var.set("sorry for your loss sir!!")
                    screen.update()
                    speak("sorry for your loss sir!!")
                else:
                    var.set("ok sir,  dont worry, everything will be fine, i am with you ")
                    screen.update()
                    speak("ok sir,  dont worry")
                    speak("everything will be fine")
                    speak("i am with you")

        elif "hey are you there" in query:
            var.set("yes sir, i am always here for you")
            screen.update()
            speak("yes sir, i am always here for you")
            var.set("what can i do for you sir!!")
            screen.update()
            speak("what can i do for you sir!!")

# SCREENSHOT FUNCTION
        elif 'take a screenshot' in query:
            var.set('ok sir what should be the name of file')
            screen.update()
            speak('ok sir what should be the name of file')
            name1= takeCommand()
            name= name1 + '.png'
            path = 'D:\\virtualbotss\\ss' + name
            ss= pyautogui.screenshot()
            ss.save(path)
            var.set('screenshot has been save')
            screen.update()
            speak ('screenshot has been save')

# clear history
        elif 'clear search history' in query:
            f = open('history.csv','w')
            f.truncate()
            f.close()
            var.set('search history is cleared sir')
            screen.update()
            speak('search history is cleared sir')

# show history
        elif 'show search history' in query:
            var.set('showing history sir')
            screen.update()
            speak('showing history sir')
            f = open('history.csv','r')
            text = f.read ()
            var.set(text)
            screen.update()
            print(text)
            f.close()


# global dictionary 
        elif 'meaning'in query:
            query = query.replace('what is','')
            query = query.replace('the meaning','')
            query = query.replace('of','')
            result= PyDictionary.meaning(query)
            var.set(f"the meaning for{query} is {result}")
            screen.update()
            speak(f"the meaning for{query} is {result}")

        elif 'synonym' in query:
            query = query.replace('what is','')
            query = query.replace('the synonym','')
            query = query.replace('of','')
            result= PyDictionary.synonym(query)
            var.set(f"the synonym for{query} is {result}")
            screen.update()
            speak(f"the synonym for{query} is {result}")

        elif "date" in query:
            date()


#notes 
        elif"note " in query:
            note()





    


def change_name():

  name_info = name.get()

  file=open("Assistant_name", "w")

  file.write(name_info)

  file.close()

  settings_screen.destroy()

  screen.destroy()


def change_name_window():
    
      global settings_screen
      global name


      settings_screen = Toplevel(screen)
      settings_screen.title("Settings")
      settings_screen.geometry("300x300")
      settings_screen.iconbitmap('app_icon.ico')

      
      name = StringVar()

      current_label = Label(settings_screen, text = "Current name: "+ name_assistant)
      current_label.pack()

      enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below") 
      enter_label.pack(pady=10)   
      

      Name_label = Label(settings_screen, text = "Name")
      Name_label.pack(pady=10)
     
      name_entry = Entry(settings_screen, textvariable = name)
      name_entry.pack()


      change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
      change_name_button.pack(pady=10)


def info():
    
  info_screen = Toplevel(screen)
  info_screen.title("Info")
  info_screen.iconbitmap('app_icon.ico')

  creator_label = Label(info_screen,text = "Created by Dhananjay chavan")
  creator_label.pack()

  Age_label = Label(info_screen, text= " It is college Project ")
  Age_label.pack()

  for_label = Label(info_screen, text = "thank you for visiting")
  for_label.pack()

keyboard.add_hotkey("F4", TaskExecution)


def wikipedia_screen(text):


  wikipedia_screen = Toplevel(screen)
  wikipedia_screen.title(text)
  wikipedia_screen.iconbitmap('app_icon.ico')

  message = Message(wikipedia_screen, text= text)
  message.pack()




screen.title(name_assistant)

screen.geometry("700x1000")
screen.maxsize(900,1200)
screen.iconbitmap('app_icon.ico')
screen.configure(bg= 'sky blue' )

name_label = Label(text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
name_label.pack()



label1 = Label(screen, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 10))
var.set('Welcome')
label1.pack(pady=5, anchor= "nw")

label2 = Label(screen, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 10))
var1.set('User Said:')
label2.pack(pady=3, anchor= "ne")



background_image =PhotoImage(file="last.png")
background_label = Label(screen, image=background_image, )
background_label.place(x=0,y=200)


microphone_photo = PhotoImage(file = "assistant_logo.png")
microphone_button = Button(image=microphone_photo, command = TaskExecution)
microphone_button.pack(pady=100)

settings_photo = PhotoImage(file = "settings.png")
settings_button = Button(image=settings_photo, command = change_name_window)
settings_button.pack(pady=5)
       
info_button = Button(text ="Info", command = info)
info_button.pack(pady=10)




screen.mainloop()


#main_screen()
