import PySimpleGUI as sg
import json
import workout_api


username = ''
password = ''


# PROGRESS BAR
def progress_bar():
    sg.theme("Topanga")
    layout = [[sg.Text('Creating your account...')],
              [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')], [sg.Cancel()]]
    window = sg.Window('Working...', layout)

    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


def create_account_window():
    global username, password
    sg.theme("Topanga")
    sg.set_options(font=('Arial Bold', 16))
    layout = [[sg.Text("Please use the drop downs below to select your profile preferences"
                       "If you are creating an account, please click 'SaveSettings' to submit. "
                       "If updating your profile: please choose a file using 'LoadSettings' "
                       "Don't forget to 'SaveSettings' at the end!", size=(55, 4), font=40)],
              [sg.Text("Create Username", size=(15, 1), font=16), sg.InputText(key='-username-', font=16)],
              [sg.Text("Create Password", size=(15, 1), font=16),
               sg.InputText(key='-password-', font=16, password_char='*')],
              [sg.Text("Set Profile Type", size=(15, 1), font=16),
               sg.OptionMenu(('Athlete', 'Coach', 'Rabbit/Pacer'), key='-typemenu-')],
              [sg.Text("Set Activity Level", size=(15, 1), font=16),
               sg.OptionMenu(('Beginner', 'Intermediate', 'Semi-Pro', 'Professional'), key='-levelmenu-')],
              [sg.Text("Set Workout Goals", size=(15, 1), font=16),
               sg.OptionMenu(('Endurance', 'Build Muscle', 'Hybrid'), key='-goalsmenu-')],
              [sg.Text("Set Radius", size=(15, 1), font=16),
               sg.OptionMenu(('5 mi', '10 mi', '25 mi'), key='-radiusmenu-')],
              [sg.Text("Set Preferred Workout Time", size=(25, 1), font=16),
               sg.OptionMenu(('Morning', 'Afternoon', 'Evening'), key='-TODmenu-')],

              [sg.Text('_' * 80)],
              [sg.Button('Cancel'),
               sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]]

    window = sg.Window("Profile", layout)

    return window


def save_settings(values):
    profile = {'-username-': values['-username-'], '-typemenu-': values['-typemenu-'],
               '-levelmenu-': values['-levelmenu-'], '-goalsmenu-': values['-goalsmenu-'],
               '-TODmenu-': values['-TODmenu-']}
    f = open("profile.txt", 'w')
    json.dump(profile, f)
    f.close()


def load_settings(window):
    f = open("profile.txt", 'r')
    profile = json.load(f)
    window['-username-'].update(value=profile['-username-'])
    window['-typemenu-'].update(value=profile['-typemenu-'])
    window['-levelmenu-'].update(value=profile['-levelmenu-'])
    window['-goalsmenu-'].update(value=profile['-goalsmenu-'])
    window['-TODmenu-'].update(value=profile['-TODmenu-'])


def create_account():
    window = create_account_window()
    while True:
        event, values = window.read()
        if event == 'SaveSettings':
            save_settings(values)
            sg.popup("Settings saved. Click 'ok' to continue")
            break

        elif event == 'LoadSettings':
            load_settings(window)

        elif event in ('Cancel', None):
            break
        else:
            if event == "Submit":
                password = values['-password-']
                username = values['-username-']
                sg.popup("Account created! Welcome to UberFIT! Please login to continue")
            break
    window.close()


def build_splash_screen():
    sg.theme("Topanga")
    layout = [[sg.Text("Welcome to UberFIT! Choose from the options below to get started.",
                       size=(50, 2), font=40, justification='c')],
              [sg.Text(" " * 100), sg.Button('Profile')],
              [sg.Button('Find a Coach'), sg.Button('Find Athletes'),
               sg.Button('Find a Pacer'), sg.Button('Request Workout')]]

    window = sg.Window("Welcome Page", layout)

    return window


def welcome_page():
    window = build_splash_screen()

    while True:
        event, values = window.read()
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
            if event == "Request Workout":
                request_workout()

    window.close()


def build_pacer_window():
    layout = [[sg.Text("Choose from the pacing athletes below:", size=(30, 3), font=16),
               sg.OptionMenu(('Alex (Beginner)', 'Moriah (Intermediate)', 'Carson (Semi-Pro)', 'Dylan (Pro)'),
                             key='Pacersmenu')],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Find Pacer Page", layout)

    return window


def find_pacer():
    window = build_pacer_window()

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                sg.popup("Have a great run! Your pacer will be in touch soon!")
                break
    window.close()


def build_find_athletes_window():
    layout = [[sg.Text("Choose from the athletes below:", size=(30, 3), font=16),
               sg.OptionMenu(('Alex', 'Moriah', 'Carson'), key='Athletesmenu')],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Find Athlete Page", layout)

    return window


def find_athletes():
    window = build_find_athletes_window()

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                sg.popup("Have a great run! The athlete you chose will be in touch soon")
                break
    window.close()


def find_coach_window():
    layout = [[sg.Text("Choose from the available coaches below:", size=(30, 3), font=16),
               sg.OptionMenu(('Coach Sloane', 'Coach Moriah', 'Coach John', 'Coach Buckley'), key='Coachesmenu')],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Find Coach Page", layout)

    return window


def find_a_coach():
    window = find_coach_window()

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                sg.popup("Have a great run! Your selected coach will reach out to you soon")
                break
    window.close()


def request_workout_window():
    layout = [[sg.Text("Enter Workout Type (Endurance, Hybrid, or Build Muscle): ", size=(30, 3)),
               sg.Input(key='-programName-', do_not_clear=True, size=(20, 1))],
              [sg.Button("Request Workout"), sg.Button("Cancel")],
              [sg.Text('Monday: ', size=(10, 1)), sg.Text(size=(100, 8), justification='left', key='-MONDAY-')],
              [sg.Text('Tuesday: ', size=(10, 1)), sg.Text(size=(100, 5), justification='left', key='-TUESDAY-')],
              [sg.Text('Wednesday: ', size=(10, 1)), sg.Text(size=(100, 5), justification='left', key='-WEDNESDAY-')],
              [sg.Text('Thursday: ', size=(10, 1)), sg.Text(size=(100, 5), justification='left', key='-THURSDAY-')],
              [sg.Text('Friday: ', size=(10, 1)), sg.Text(size=(100, 5), justification='left', key='-FRIDAY-')],
              [sg.Text('Saturday: ', size=(10, 1)), sg.Text(size=(100, 5), justification='left', key='-SATURDAY-')],
              [sg.Text('Sunday: ', size=(10, 1)), sg.Text(size=(100, 5), justification='left', key='-SUNDAY-')],
              ]

    window = sg.Window("Request a Workout Page", layout)
    return window


def request_workout():
    window = request_workout_window()

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if event == "Request Workout":
            workout_info = workout_api.request_workout_info(values['-programName-'])
            window['-MONDAY-'].update(workout_info['monday'])
            window['-TUESDAY-'].update(workout_info['tuesday'])
            window['-WEDNESDAY-'].update(workout_info['wednesday'])
            window['-THURSDAY-'].update(workout_info['thursday'])
            window['-FRIDAY-'].update(workout_info['friday'])
            window['-SATURDAY-'].update(workout_info['saturday'])
            window['-SUNDAY-'].update(workout_info['sunday'])
    window.close()


def build_login_window():
    global username, password
    sg.theme("Topanga")
    layout = [[sg.Text("Welcome to UberFIT! If you have an account, please log in. "
                       "Otherwise, select 'Register' to set up a free account and start finding "
                       "coaches and athletes today!", size=(55, 3), font=40, justification='c')],
              [sg.Text("Username", size=(15, 1), font=16), sg.InputText(key='-usrnm-', font=16)],
              [sg.Text("Password", size=(15, 1), font=16), sg.InputText(key='-pwd-', password_char='*', font=16)],
              [sg.Button('Login'), sg.Button('Register')]]

    window = sg.Window("Log In", layout)
    return window


def login():
    window = build_login_window()

    while True:
        event, values = window.read()
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
