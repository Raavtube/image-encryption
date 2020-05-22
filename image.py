#!/usr/bin/python3
from tkinter import Label, Tk
from PIL import Image, ImageTk
import tkFileDialog
root = Tk()

path = tkFileDialog.askopenfilename(filetypes=[("Image File", '.jpg')])
im = Image.open(path)
tkimage = ImageTk.PhotoImage(im)
myvar = Label(root, image=tkimage)
myvar.image = tkimage
myvar.pack()

root.mainloop()