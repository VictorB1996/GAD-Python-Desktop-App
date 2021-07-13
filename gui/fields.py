import tkinter


class Field:
    def __init__(self, root, label_text):
        self.label = tkinter.Label(root, text=label_text)
        self.label.pack()
        self.entry = tkinter.Entry(root)
        self.entry.pack()
