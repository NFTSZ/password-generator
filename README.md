# Password Generator with PySimpleGUI

This is a simple password generator GUI application built using the PySimpleGUI library in Python. The application allows you to generate a specified number of random passwords with a specified length and view them in a separate window.

## Requirements

- Python 3.x
- PySimpleGUI library

## Installation

1. Install Python from the official website: https://www.python.org/downloads/
2. Install the PySimpleGUI library using pip:

       pip install PySimpleGUI

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script:

       python main.py or python3 main.py
 
5. The main window will appear with fields to specify the number of passwords to generate and their length.
6. Click the "Show Passwords" button.
7. A new window will appear displaying the generated passwords.
8. Close the password display window by clicking the "OK" button.
9. Close the main window to exit the application.

## Code Explanation

- The script defines a function `showPass(num_pass, len_pass)` that generates random passwords based on the specified parameters.
- The main window layout is created using the PySimpleGUI library, featuring input fields and a "Show Passwords" button.
- The script enters a loop to read events from the main window. If the "Show Passwords" button is clicked, a new window with the generated passwords is displayed using the layout specified.
- The script employs PySimpleGUI's event-driven approach to handle user interactions and window updates.
