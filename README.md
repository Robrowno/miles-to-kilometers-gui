# miles-to-kilometers-gui
A simple GUI app that converts Miles to KM - Following 10 Python apps with tkinter course on Udemy

![GUI Miles to Kilometers Converter](/assets/gui_screenshot.png "Mi to Km Converter App")


## Course Material
If you are interested in looking in to GUI or this course spcifically, check out here ---> https://www.udemy.com/course/learn-python-by-creating-10-apps/

## L.O's

- Learn how to use tkinter on VSCODE on Mac
- Set up a virtual environment to begin working on the local repo
- Follow the tutorial for the first GUI app for a simple Mi->Km converter
- Push local code up to a repo on Github
- Demo App and play around with different variables and values


# Initialising VSCode & tkinter on Mac

I followed a great youtube tutorial for the basic setup, as the course tutorial uses the Sublime text editor for the material. I only opted to do this for personal choice.

- Create a Folder and open it through VSCode
- Create a python file, for example, main.py
- active your virtual environment, this can be done by typing out `python3 -m venv [A name for your VENV] in the CLI`
- To active your virtual environment, type `source [Your VENV]/bin/activate
- You should see your folder name in parentheses in your CLI when your venv is activated.
- tkinker is included in the python3 library, so your can import it into your main.py file by typing `import tkinter` or `from tkinter import *` or any other specific import you need.
- To check all is working you can type something like this:

    ```
    from tkinter import *

    main = Tk()

    main.mainloop()
```

- When you run the app by clicking the 'Play' run button on the top left of your VSCode window, an app pop-up should appear if all is working like so:

![Empty GUI window](/assets/my_first_gui.png)






