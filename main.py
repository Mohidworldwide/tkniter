                                            #..activity 1
# from tkinter import *

# window=Tk()
# window.title('tkinter sample window')
# window.geometry('300x300')


# greeting=Label(text="hello user",fg="black",bg="yellow")

# button=Button(text="click me",bg="black",fg="white")

# entry=Entry(fg="yellow",bg="blue",width=50)

# greeting.pack()
# button.pack()
# entry.pack()

# frame=Frame(master="window",relief=RAISED,borderwidth=5)
# frame.pack()
# label=Label(master=frame,text='sample frame')
# label.pack()


# textbox=Text(fr="green",bg="yellow")



                                                #..activity2

import tkinter as tk

window = tk.Tk()

for i in range(3):

    for j in range(3):

        frame = tk.Frame(

master=window,

relief=tk.RAISED,

borderwidth=1

)

        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")

        label.pack()

window.mainloop()

