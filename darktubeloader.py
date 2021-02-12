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
            [sg.Button('MP3 One'),sg.Button('MP3 List'),sg.Button('Video One'),sg.Button('Video List'),sg.Button('Folder'),sg.Button('Exit')]
            ]

# Create the window
window = sg.Window('Dark Tube Loader', layout)      # Part 3 - Window Defintion

while(True):
    
    # Display and interact with the Window
    event, values = window.read()                   # Part 4 - Event loop or Window.read call
    if ('One' in event) or ('List' in event):
        command = f"{simple_path}\\external\\youtube-dl.exe -i -R 10"

        if 'One' in event:
            command += " --no-playlist"
        else:
            command += " --yes-playlist"

        if 'MP3' in event:
            command += f" --extract-audio --audio-format mp3"
            command += f" --ffmpeg-location \"{simple_path}\"\\external\\ffmpeg.exe"

        command += f" -o download\\%(title)s-%(id)s.%(ext)s"
        command += f" \"{values[0]}\""

        os.system(command)
    else:
        if (event == 'Folder'):
            os.startfile(f'{simple_path}\\download')
        if (event == 'Exit'):
            break

    # Do something with the information gathered
    print('Operation has been finished')
 
# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window