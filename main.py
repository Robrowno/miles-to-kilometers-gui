import tkinter as tk 
# from tkinter import *
import ttkbootstrap as ttk

def convert():
	mile_input = entry_int.get()
	km_output = mile_input * 1.60934 # conversion value from Google
	# Setting output string to km value
	output_string.set(km_output)

# window 
window = ttk.Window(themename = 'darkly') # bootstrap dark theme
window.title('Miles --> Kilometers')
window.geometry('300x150') # set window size to 300px by 150px

# title 
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

# input field 
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
	master = window, 
	text = 'Output', 
	font = 'Calibri 24', 
	textvariable = output_string)
output_label.pack(pady = 5)

# run 
window.mainloop()