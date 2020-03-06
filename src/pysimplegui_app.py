import sys

import PySimpleGUI as sg

if len(sys.argv) > 1:

    command = sys.argv[1]

    print(f"CLI app. Command is: {command}")

else:

    print("GUI app.")

    sg.theme("DarkAmber")

    layout = [
        [sg.Text('Some text on Row 1')],
        [sg.Text('Enter something on Row 2'), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')],
    ]

    window = sg.Window('Window Title', layout=layout)

    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            print('Good bye!')
            break
        print('You entered ', values[0])

    window.close()
