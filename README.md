# NOVI_Programming_Fundamentals
Module Programming fundamentals voor NOVI Hogeschool

## Installation
1. Install Python: ```https://www.python.org/downloads/``` for the latest version
   1. Recommended: python 3.10 or above
2. Install the requirements using: ```pip install -r requirements.txt```
   1. Make sure you opened the console from the same folder this readme is in.
   2. if this doesn't work manually install the keyboard modules:
      1. ```https://pypi.org/project/keyboard/```
      2. ```https://pypi.org/project/requests/```
3. Run main.py to start the application.
   1. Using PyCharm: select your python version and click the green arrow
   2. Using the command line: ```<path-to-your-python.exe> <path-to-this-folder>/main.py```  (backslash for windows)

### Known Bugs
* PyCharm Powershell doesn't overwrite the first time you change choice_menu options.
  * workaround: open main.py through a regular terminal/command prompt:
    ```<path-to-your-python.exe> <path-to-this-folder>/main.py``` (backslash for windows)
* After the program completes, multiple outputs are generated on the command line. 
This is a bug in the keyboard module, but does not impact the game.
