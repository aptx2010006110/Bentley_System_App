import tkinter as tk

windows = tk.Tk()
windows.title("Bentley System")
windows.geometry("1280x720")

image = tk.PhotoImage(file="microstation.png")
image_width = 586
image_height = 535

button_width = 15
button_height = 2

substation_button = tk.Button(windows, text="Substation", width=button_width, height=button_height,activebackground='gray',borderwidth=3,relief='raised')

def enter(event):
    global label
    label = tk.Label(windows,image=image)
    label.place(x=200 + button_width, y=20)
def leave(event):
    label.place_forget()
def show_microstation_interface():
    substation_button.destroy()
    # substation_image_label.destroy()   