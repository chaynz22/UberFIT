import os
import PySimpleGUI as sg
from dotenv import load_dotenv
from dotenv import dotenv_values

# load_dotenv()
#
# config = {
#     **dotenv_values(".env.shared"),  # load shared development variables
#     **dotenv_values(".env.secret"),  # load sensitive variables
#     **os.environ,  # override loaded values with environment variables
# }
username = ''
password = ''


# PROGRESS BAR
def progress_bar():
    sg.theme("Topanga")
    layout = [[sg.Text('Creating your account...')],
            [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
            [sg.Cancel()]]

    window = sg.Window('Working...', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


def create_account():
    global username, password
    sg.theme("Topanga")
    layout = [[sg.Text("Sign Up", size =(15, 1), font=40)],
             # [sg.Text("E-mail", size =(15, 1),font=16), sg.InputText(key='-email-', font=16)],
             # [sg.Text("Re-enter E-mail", size=(15, 1), font=16), sg.InputText(key='-remail-', font=16)],
     [sg.Text("Create Username", size =(15, 1), font=16), sg.InputText(key='-username-', font=16)],
     [sg.Text("Create Password", size =(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
     [sg.Text("Set Profile Type", size =(15, 1), font=16),
      sg.OptionMenu(('Athlete', 'Coach', 'Rabbit/Pacer'), key='typemenu')],

     [sg.Text("Set Activity Level", size=(15, 1), font=16),
        sg.OptionMenu(('Beginner', 'Intermediate', 'Semi-Pro', 'Professional'), key='levelmenu')],

     [sg.Text("Set Radius", size=(15, 1), font=16),
        sg.OptionMenu(('5 mi', '10 mi', '25 mi'), key='radiusmenu')],

     [sg.Text("Set Preferred Workout Time", size=(15, 1), font=16),
        sg.OptionMenu(('Morning', 'Afternoon', 'Evening'), key='TODmenu')],

     [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Sign Up", layout)

    while True:
        event,values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                password = values['-password-']
                username = values['-username-']
                sg.popup("Account created! Welcome to UberFIT! Please login to continue")
            break
    window.close()

#
# create_account()


def login():
    global username,password
    sg.theme("Topanga")
    layout = [[sg.Text("Welcome to UberFIT! If you have an account, please log in. "
                       "Otherwise, select 'Register' to set up a free account", size =(50, 2), font=40,
                       justification='c')],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-usrnm-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
            [sg.Button('Login'), sg.Button('Register')]]

    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Register":
            create_account()
        else:
            if event == "Login":
                if values['-usrnm-'] == username and values['-pwd-'] == password:
                    sg.popup("Welcome to UberFIT!")
                    break
                elif values['-usrnm-'] != username or values['-pwd-'] != password:
                    sg.popup("Invalid login. Try again")

    window.close()


def main():
    login()



if __name__ == '__main__':
    main()
