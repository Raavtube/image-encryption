#!/usr/bin/python3
from tkinter import Label, Tk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import shutil
from cryptography.fernet import Fernet
root = tk.Tk()

# ----------------- Getting the current directory -------------------------

filePath = __file__
fileName = os.path.basename(__file__)
filePath = filePath.replace(fileName, "")
print(filePath)

# ----------------- Creating temp directory -------------------------
try:
    os.mkdir(filePath + "temp")
except:
    print("Unable to create temp directory, probably bad permissions or directory is already created.")
filepath = filePath + "temp"
print(filePath)

try:
    os.mkdir(filePath + "encrypted")
except:
    print("Unable to create temp directory, probably bad permissions or directory is already created.")

print(filePath)


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def encryptImage():
    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
    print(path)
    tempImageName = "IMAGEX1.jpg"
    print(tempImageName)
    imagePath = filePath + "temp/" + tempImageName
    print(imagePath)
    shutil.copyfile(path, imagePath)
    # ----------------- ENCRYPTTING THE IMAGE -----------------------
    write_key()
    key = load_key()
    encrypt(imagePath, key)


frame = tk.Frame(root)
frame.pack(padx=20, pady=40)

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Select Image to encrypt.",
                   command=encryptImage)
slogan.pack(side=tk.LEFT, padx=10)


root.mainloop()
