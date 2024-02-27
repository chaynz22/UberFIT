import os
import PySimpleGUI as sg
import json
import socket
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
    sg.set_options(font=( 'Arial Bold', 16))
    layout = [[sg.Text("Please use the drop downs below to select your profile preferences"
                       "If you are creating an account, please click 'SaveSettings' to submit. "
                       "If updating your profile: please choose a file using 'LoadSettings' "
                       "Don't forget to 'SaveSettings' at the end!", size =(55, 4), font=40)],
             # [sg.Text("E-mail", size =(15, 1),font=16), sg.InputText(key='-email-', font=16)],
             # [sg.Text("Re-enter E-mail", size=(15, 1), font=16), sg.InputText(key='-remail-', font=16)],
     [sg.Text("Create Username", size =(15, 1), font=16), sg.InputText(key='-username-', font=16)],
     [sg.Text("Create Password", size =(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
     [sg.Text("Set Profile Type", size =(15, 1), font=16),
      sg.OptionMenu(('Athlete', 'Coach', 'Rabbit/Pacer'), key='-typemenu-')],
     [sg.Text("Set Activity Level", size=(15, 1), font=16),
        sg.OptionMenu(('Beginner', 'Intermediate', 'Semi-Pro', 'Professional'), key='-levelmenu-')],
     [sg.Text("Set Workout Goals", size=(15, 1), font=16),
        sg.OptionMenu(('Basic Fitness', 'Endurance', 'Strength', 'CrossTraining'), key='-goalsmenu-')],
     [sg.Text("Set Radius", size=(15, 1), font=16),
        sg.OptionMenu(('5 mi', '10 mi', '25 mi'), key='-radiusmenu-')],
     [sg.Text("Set Preferred Workout Time", size=(25, 1), font=16),
        sg.OptionMenu(('Morning', 'Afternoon', 'Evening'), key='-TODmenu-')],

     [sg.Text('_' * 80)],
     # [sg.Text('Choose A Folder', size=(35, 1))],
     # [sg.Text('Your Folder', size=(15, 1), justification='right'),
     #    sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
     [sg.Button('Cancel'),
        sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]]

    window = sg.Window("Profile", layout)

    while True:
        event,values = window.read()
        if event == 'SaveSettings':
            profile = {'-username-': values['-username-'], '-typemenu-': values['-typemenu-'],
                       '-levelmenu-': values['-levelmenu-'], '-goalsmenu-': values['-goalsmenu-'],
                       '-TODmenu-': values['-TODmenu-']}
            f = open("profile.txt", 'w')
            json.dump(profile, f)
            f.close()
            # filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            # window.SaveToDisk(filename)
            password = values['-password-']
            username = values['-username-']

            sg.popup("Settings saved. Click 'ok' to continue")
            break
            # save(values)
        elif event == 'LoadSettings':
            f = open("profile.txt", 'r')
            profile = json.load(f)
            window['-username-'].update(value=profile['-username-'])
            window['-typemenu-'].update(value=profile['-typemenu-'])
            window['-levelmenu-'].update(value=profile['-levelmenu-'])
            window['-goalsmenu-'].update(value=profile['-goalsmenu-'])
            window['-TODmenu-'].update(value=profile['-TODmenu-'])
            # filename = sg.popup_get_file('Load Settings', no_window=True)
            # window.LoadFromDisk(filename)
            # load(form)
        elif event in ('Cancel', None):
            break
        else:
            if event == "Submit":
                password = values['-password-']
                username = values['-username-']
                sg.popup("Account created! Welcome to UberFIT! Please login to continue")
            break
    window.close()


def welcome_page():
    sg.theme("Topanga")
    layout = [[sg.Text("Welcome to UberFIT! Choose from the options below to get started.",
                       size=(50, 2), font=40, justification='c')],
              [sg.Text(" " * 40), sg.Button('Profile',)],
              [sg.Button('Find a Coach'), sg.Button('Find Athletes'),
                 sg.Button('Find a Pacer'), sg.Button('Send Profile to Request Workout')]]

    # ** coming soon to a theater near you : sg.Button('Request a workout') **

    window = sg.Window("Welcome Page", layout)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            if event == "Profile":
                create_account()
            if event == "Find a Coach":
                find_a_coach()
            if event == "Find Athletes":
                find_athletes()
            if event == "Find a Pacer":
                find_pacer()
            if event == "Send Profile to Request Workout":
                request_workout()

    window.close()


def find_pacer():
    layout = [[sg.Text("Choose from the pacing athletes below:", size=(30, 3), font=16),
               sg.OptionMenu(('Alex (Beginner)', 'Moriah (Intermediate)', 'Carson (Semi-Pro)', 'Dylan (Pro)'),
                             key='Pacersmenu')],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Find Pacer Page", layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                sg.popup("Have a great run! Your pacer will be in touch soon!")
                break
    window.close()


def find_athletes():
    layout = [[sg.Text("Choose from the athletes below:", size=(30, 3), font=16),
     sg.OptionMenu(('Alex', 'Moriah', 'Carson'), key='Athletesmenu')],
    [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Find Athlete Page", layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                sg.popup("Have a great run! The athlete you chose will be in touch soon")
                break
    window.close()


def find_a_coach():
    layout = [[sg.Text("Choose from the available coaches below:", size=(30, 3), font=16),
               sg.OptionMenu(('Coach Sloane', 'Coach Moriah', 'Coach John', 'Coach Buckley'), key='Coachesmenu')],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Find Coach Page", layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                sg.popup("Have a great run! Your selected coach will reach out to you soon")
                break
    window.close()


def request_workout():
    layout = [[sg.Text("Enter Profile Filename (default is profile.txt): ", size=(30, 3), font=16),
               sg.InputText()],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Request a Workout Page", layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            host = '127.0.0.1'
            port = 8080

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connecting with Server
            sock.connect((host, port))

            filename = values[0]

            # Reading file and sending data to server
            fi = open(filename, "r")
            data = fi.read()
            if not data:
                break
            while data:
                sock.send(str(data).encode())
                data = fi.read()
                # File is closed after data is sent
            fi.close()
            break
    window.close()





def login():
    global username,password
    sg.theme("Topanga")
    layout = [[sg.Text("Welcome to UberFIT! If you have an account, please log in. "
                       "Otherwise, select 'Register' to set up a free account and start finding "
                       "coaches and athletes today!",
                       size =(55, 3), font=40, justification='c')],
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
                    welcome_page()
                    break
                elif values['-usrnm-'] != username or values['-pwd-'] != password:
                    sg.popup("Invalid login. Try again")

    window.close()


def main():
    login()


if __name__ == '__main__':
    main()
