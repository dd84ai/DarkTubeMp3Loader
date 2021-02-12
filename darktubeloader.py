import PySimpleGUI as sg                        # Part 1 - The import
import os  
import pathlib
path = pathlib.Path(__file__).parent.absolute()
simple_path = rf'{path}'
#print(simple_path)

if not os.path.exists('download'):
    os.makedirs('download')

# Define the window's contents
layout = [  [sg.Text("Insert youtube link here")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Text("Example for one: https://www.youtube.com/watch?v=EdjMNDZb4_E")], 
            [sg.Text("Example for playlist: https://www.youtube.com/playlist?list=PLEFBA46183C537494")], 
            [sg.Text("Choose to load one song or playlist into mp3 format")], 
            [sg.Button('One MP3'),sg.Button('List MP3'),sg.Button('Folder'),sg.Button('Exit')]
            ]

# Create the window
window = sg.Window('Dark Tube MP3 Loader', layout)      # Part 3 - Window Defintion

while(True):
    
    # Display and interact with the Window
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    if (event == 'One MP3' or event == 'List MP3'):
        command1 = f"{simple_path}\\external\\youtube-dl.exe -i -R 10 --extract-audio --audio-format mp3"

        if (event == 'One MP3'):
            command2 = " --no-playlist"
        else:
            command2 = " --yes-playlist"

        command3 = f" --ffmpeg-location \"{simple_path}\"\\external\\ffmpeg.exe"
        command4 = f" -o download\\%(title)s-%(id)s.%(ext)s"
        command5 = f" \"{values[0]}\""

        os.system(command1 + command2 + command3 + command4 + command5)
    else:
        if (event == 'Folder'):
            os.startfile(f'{simple_path}\\download')
        if (event == 'Exit'):
            break

    # Do something with the information gathered
    print('Operation has been finished')
 
# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window