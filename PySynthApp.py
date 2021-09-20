import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=300, bg="#8cb923")
canvas.pack()

header = tk.Frame(root, bg="#3C00E0")
header.place(relwidth=1, relheight=0.2)

#C
c_key = tk.Button(root, text="C", padx=25, pady=100, bg="#8cb923")
c_key.pack(side=tk.LEFT)

#C-Sharp
c_sh_key = tk.Button(root, text="C#", padx=25, pady=100, fg= "black", bg="black")
c_sh_key.pack(side=tk.LEFT)

#D
d_key = tk.Button(root, text="D", padx=25, pady=100, bg="#8cb923")
d_key.pack(side=tk.LEFT)

#D-Sharp
d_sh_key = tk.Button(root, text="D#", padx=25, pady=100, bg="#8cb923")
d_sh_key.pack(side=tk.LEFT)

#E
e_key = tk.Button(root, text="E", padx=25, pady=100, bg="#8cb923")
e_key.pack(side=tk.LEFT)

#F
f_key = tk.Button(root, text="F", padx=25, pady=100, bg="#8cb923")
f_key.pack(side=tk.LEFT)

#F-Sharp
f_sh_key = tk.Button(root, text="F#", padx=25, pady=100, bg="#8cb923")
f_sh_key.pack(side=tk.LEFT)

#G
g_key = tk.Button(root, text="G", padx=25, pady=100, bg="#8cb923")
g_key.pack(side=tk.LEFT)

#G-Sharp
g_sh_key = tk.Button(root, text="G#", padx=25, pady=100, bg="#8cb923")
g_sh_key.pack(side=tk.LEFT)

#A
a_key = tk.Button(root, text="A", padx=25, pady=100, bg="#8cb923")
a_key.pack(side=tk.LEFT)

#A-Sharp
a_sh_key = tk.Button(root, text="A#", padx=25, pady=100, bg="#8cb923")
a_sh_key.pack(side=tk.LEFT)

#B
b_key = tk.Button(root, text="B", padx=25, pady=100, bg="#8cb923")
b_key.pack(side=tk.LEFT)

root.mainloop()
