import scrap as sc
from Tkinter import *
import Tkinter as tk

r = tk.Tk()
x = vars()
l1 = Label(r, text="Enter URL", bg="#a1dbcd", width=15, height=2)
e1 = Entry(r, textvariable=x, width=35)
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
b1 = Button(r, text="FIND", fg="#a1dbcd", bg="#383a39", command=lambda: sc.func(e1.get()))
b1.grid(row=1, column=0)

instructions = "GeT The NET"
Instruct = Label(width=15, height=3, text=instructions, justify=LEFT, bg="#C8F9C4")
Instruct.grid(row=1, column=1, padx=10, pady=2)

colorLog = Text(width=150, height=50, highlightthickness=1, fg="#383a39", bg="#a1dbcd")
colorLog.grid(row=3, column=0, padx=10, pady=10)
b2 = Button(r, text="RESULT", fg="#a1dbcd", bg="#383a39", command=lambda: colorLog.insert(0.0, sc.func(e1.get())))
b2.grid(row=2, column=0)
r.mainloop()
