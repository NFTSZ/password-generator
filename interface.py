import PySimpleGUI as sg
import random

# Define the characters that can be used in passwords
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*_'

# Function to generate passwords
def showPass(num_pass, len_pass):
    passwords = []
    for pss in range(num_pass):
        password = ''
        for n in range(len_pass):
            password += random.choice(chars)
        #print(password)'''
        passwords.append(password)
    return passwords
            
# Main window layout
sg.theme('Default1')  # Define o tema da interface gráfica
layout = [
    [sg.Text('Number of passwords: '), sg.Input(key='nPass', size=(7, 1))],  
    [sg.Text('Length of password:'), sg.Input(key='lPass', size=(7, 1))],  
    [sg.Button('Show Passwords', key='show', size=(12, 1))]
]

# Create the main window
window = sg.Window('Password Generator', layout) 

while True:
    eventos, valores = window.read()  # Read events from the window
    if eventos == sg.WINDOW_CLOSED:  # Check if the window was closed
        break  # End the loop

    if eventos == 'show':
        num_pass = int(valores['nPass'])  # Get the number of passwords to generate
        len_pass = int(valores['lPass'])  # Get the length of each password
        passwords = showPass(num_pass, len_pass)  # Generate passwords
        
        # Layout for the results window
        result_layout = [
            [sg.Text('Generated Passwords:')],
            [sg.Multiline('\n'.join(passwords), size=(40, 10))],
            [sg.Button('OK')]
        ]
        
        # Create and display the results window
        result_window = sg.Window('Generated Passwords', result_layout)
        result_event, _ = result_window.read()  # Wait for an event in the results window
        result_window.close()  # Close the results window
        
window.close() # Close the main window when the loop ends


