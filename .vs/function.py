def enter(event):
    global label
    label = tk.Label(windows,image=image)
    label.place(x=200 + button_width, y=20)
def leave(event):
    label.place_forget()