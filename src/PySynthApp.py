import tkinter as tk
import tkmacosx as tkmc
# from tkinter import filedialog, Text
import PyoFunctionality as PF

root = tk.Tk()
root.title("PySynth")
root.geometry("1000x500")

# White Keys

# C
c_key = tkmc.Button(root, padx=25, pady=100, bg='white', command=lambda: PF.play_key('C'))
c_key.grid(row=0, column=0, rowspan=2, columnspan=3, sticky='nsew')

# D
d_key = tkmc.Button(root, padx=25, pady=100, bg='white', command=PF.play_key('D'))
d_key.grid(row=0, column=3, rowspan=2, columnspan=3, sticky='nsew')

# E
e_key = tkmc.Button(root, padx=25, pady=100, bg='white', command=PF.play_key('E'))
e_key.grid(row=0, column=6, rowspan=2, columnspan=3, sticky='nsew')

# F
f_key = tkmc.Button(root, padx=25, pady=100, bg='white', command=PF.play_key('F'))
f_key.grid(row=0, column=9, rowspan=2, columnspan=3, sticky='nsew')

# G
g_key = tkmc.Button(root, padx=25, pady=100, bg='white', command=PF.play_key('G'))
g_key.grid(row=0, column=12, rowspan=2, columnspan=3, sticky='nsew')

# A
a_key = tkmc.Button(root, padx=25, pady=100, bg='white', command=PF.play_key('A'))
a_key.grid(row=0, column=15, rowspan=2, columnspan=3, sticky='nsew')

# B
b_key = tkmc.Button(root, padx=25, pady=100, bg='white', command=PF.play_key('B'))
b_key.grid(row=0, column=18, rowspan=2, columnspan=3, sticky='nsew')

# Black Keys

# C-Sharp
c_sh_key = tkmc.Button(root, padx=13, pady=5, bg='black', command=PF.play_key('C#'))
c_sh_key.grid(row=0, column=2, rowspan=1, columnspan=2, sticky='nsew')

# D-Sharp
d_sh_key = tkmc.Button(root, padx=13, pady=65, bg='black', command=PF.play_key('D#'))
d_sh_key.grid(row=0, column=5, rowspan=1, columnspan=2, sticky='nsew')

# F-Sharp
f_sh_key = tkmc.Button(root, padx=13, pady=65, bg='black', command=PF.play_key('F#'))
f_sh_key.grid(row=0, column=11, rowspan=1, columnspan=2, sticky='nsew')

# G-Sharp
g_sh_key = tkmc.Button(root, padx=13, pady=65, bg='black', command=PF.play_key('G#'))
g_sh_key.grid(row=0, column=14, rowspan=1, columnspan=2, sticky='nsew')

# A-Sharp
a_sh_key = tkmc.Button(root, padx=13, pady=65, bg='black', command=PF.play_key('A#'))
a_sh_key.grid(row=0, column=17, rowspan=1, columnspan=2, sticky='nsew')

for i in range(7 * 3):
    root.columnconfigure(i, weight=1)

for i in range(2):
    root.rowconfigure(i, weight=1)

def say_hello(self):
    print('Hello!')

root.mainloop()
