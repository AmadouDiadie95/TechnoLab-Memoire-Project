from tkinter import *

from  tkinter import ttk
#defining login function

global login_screen
login_screen = Tk()


def login():
    # getting form data
    uname = username.get()
    pwd = password.get()
    # applying empty validation
    if uname == '' or pwd == '':
        message.set("fill the empty field!!!")
    else:
        if uname == "azerty" and pwd == "123":
            message.set("Login success")
            login_screen.destroy()
            import project
        else:
            message.set("Wrong username or password!!!")
# defining loginform function



#Setting title of screen
login_screen.title("Veuillez vous Connecter")
#setting height and width of screen
login_screen.geometry("300x250")
#declaring variable
global  message;
global username
global password
username = StringVar()
password = StringVar()
message=StringVar()
# Create an object of tkinter ImageTk

# Create a Label Widget to display the text or Image
#Creating layout of login form
Label(login_screen,width="300", text="Entrez Vos identitfiants", bg="orange",fg="white").pack()
#Username Label
Label(login_screen, text="Username * ").place(x=20,y=40)
#Username textbox
Entry(login_screen, textvariable=username).place(x=90,y=42)
#Password Label
Label(login_screen, text="Password * ").place(x=20,y=80)
#Password textbox
Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
#Label for displaying login status[success/failed]
Label(login_screen, text="",textvariable=message).place(x=95,y=100)
#Login button
Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105,y=130)
login_screen.mainloop()



