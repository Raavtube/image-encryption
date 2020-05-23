#!/usr/bin/python3
from tkinter import Label, Tk
from PIL import Image, ImageTk
from tkinter import filedialog
root = Tk()

path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
im = Image.open(path)
tkimage = ImageTk.PhotoImage(im)
print(path)
myvar = Label(root, image=tkimage)
myvar.image = tkimage
myvar.pack()

root.mainloop()
