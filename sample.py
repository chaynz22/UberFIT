import PySimpleGUI as sg
import socket
import json

if __name__ == '__main__':

    layout = [[sg.Text("Click 'Submit' below to request a profile from which to create a workout."
                       "Or click 'Cancel' to quit this application", size=(30, 3), font=16),],
              [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Send Profile Request", layout)

    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":# Defining Socket
                host = '127.0.0.1'
                port = 8080
                totalclient = int(input('Enter number of clients: '))

                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind((host, port))
                sock.listen(totalclient)
                # Establishing Connections
                connections = []
                print('Initiating clients and requesting profiles')
                for i in range(totalclient):
                    conn = sock.accept()
                    connections.append(conn)
                    print('Connected with client', i + 1)

                idx = 0
                for conn in connections:
                    # Receiving File Data
                    idx += 1
                    data = conn[0].recv(1024).decode()

                    if not data:
                        continue

                    string = json.loads(data)
                    un = ''
                    for i in string['-username-']:
                        un += i
                    # Creating a new file at server end and writing the data
                    filename = str(un) + '_profile' + '.txt'
                    fo = open(filename, "w")
                    while data:
                        if not data:
                            break
                        else:
                            fo.write(data)
                            data = conn[0].recv(1024).decode()

                    print()
                    print('Receiving file from client', idx)
                    print()
                    print('Received successfully! New filename is:', filename)
                    fo.close()
                # Closing all Connections
                for conn in connections:
                    conn[0].close()


                break
    window.close()


