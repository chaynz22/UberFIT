import socket
import PySimpleGUI as sg


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
            print("Sending profile to sample program")
            fi = open(filename, "r")
            data = fi.read()
            if not data:
                break
            while data:
                sock.send(str(data).encode())
                data = fi.read()
                # File is closed after data is sent
            fi.close()
            print("Profile sent successfully. You will receive a workout shortly.")
            break
    window.close()

