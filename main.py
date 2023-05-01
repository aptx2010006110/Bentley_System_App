import tkinter as tk
from function import enter,leave,show_microstation_interface

windows = tk.Tk()
windows.title("Bentley System")
windows.geometry("1280x720")


bg_img = tk.PhotoImage(file="bentley.png")
bg_canvas = tk.Canvas(windows, width=728, height=676)
bg_canvas.pack()
bg_canvas.create_image(0, 0, image=bg_img, anchor="nw")
bg_canvas.place(relx=1, rely=1, anchor="se", x=400, y=470)

image = tk.PhotoImage(file="microstation.png")
image_width = 586
image_height = 535

button_width = 15
button_height = 2
microstation_button = tk.Button(windows, text="Microstation", width=button_width, height=button_height,activebackground='gray',borderwidth=3,relief='raised',command=show_microstation_interface)
microstation_button.place(x=20, y=20)
microstation_button.bind('<Enter>',enter,100)
microstation_button.bind('<Leave>',leave,100)
substation_button = tk.Button(windows, text="Substation", width=button_width, height=button_height,activebackground='gray',borderwidth=3,relief='raised')
substation_button.place(x=20, y=80)

windows.mainloop()
