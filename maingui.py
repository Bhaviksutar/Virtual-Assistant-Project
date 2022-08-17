from Virtual_Assistant import *
from tkinter import *              #For the graphics   
import keyboard
from Virtual_Assistant import TaskExecution


def change_name():
    
  name_info = name.get()

  file=open("Assistant_name", "w")

  file.write(name_info)

  file.close()

  settings_screen.destroy()

  screen.destroy()

name_file = open("Assistant_name", "r")
name_assistant = name_file.read()

def change_name_window():
    
      global settings_screen
      global name


      settings_screen = Toplevel(screen)
      settings_screen.title("Settings")
      settings_screen.geometry("300x300")
      settings_screen.iconbitmap('app_icons.png')

      
      name = StringVar()

      current_label = Label(settings_screen, text = "Current name: "+ name_assistant)
      current_label.pack()

      enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name") 
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
  info_screen.iconbitmap('app_icons.png')

  creator_label = Label(info_screen,text = "Created by Dhanajay chavan")
  creator_label.pack()

  Age_label = Label(info_screen, text= " It is college Project ")
  Age_label.pack()

  for_label = Label(info_screen, text = "thank you for visiting")
  for_label.pack()

#keyboard.add_hotkey("F4", TaskExecution)


def wikipedia_screen(text):


  wikipedia_screen = Toplevel(screen)
  wikipedia_screen.title(text)
  wikipedia_screen.iconbitmap('app_icons.png')

  message = Message(wikipedia_screen, text= text)
  message.pack()



def main_screen():
    global screen

    #query = takeCommand()
    screen = Tk()
    canvas_width = 800
    canvas_height = 400
    screen.title(name_assistant)
    screen.geometry("500x700")
    screen.maxsize(600,900)
    screen.iconbitmap('app_icons.png')

    can_widget = Canvas(screen, width=canvas_width, height=canvas_height)
    can_widget.pack()

    
    




    #query = textF.get()
    


    name_label = Label(text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
    name_label.pack()


    background_image =PhotoImage(file="last.png")
    background_label = Label(screen, image=background_image, )
    background_label.place(x=0,y=0 )


    microphone_photo = PhotoImage(file = "assistant_logo.png")
    microphone_button = Button(screen,image=microphone_photo, command = TaskExecution)
    microphone_button.pack(pady=2)

    settings_photo = PhotoImage(file = "settings.png")
    settings_button = Button(image=settings_photo, command = change_name_window)
    settings_button.pack(pady=5)
       
    info_button = Button(text ="Info", command = info)
    info_button.pack(pady=10)

    '''frame=Frame(screen)

    sc=Scrollbar(frame)

    msgs =Listbox(frame,width=40,height=10)

    sc.pack(side=RIGHT,fill=Y)
    msgs.pack(side=LEFT,fill=BOTH,pady=10)
    frame.pack()'''    

      #creating text field
    '''textF=Entry(screen,font=("verdana",20))
    textF.pack(fill=X,pady=10)'''

    #task = Thread(target= TaskExecution)
    #task.start()

   
    can_widget.create_text(10,30, text = "dany")

    screen.mainloop()
    
main_screen()

