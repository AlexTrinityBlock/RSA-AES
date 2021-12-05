from usr.HomeWorkCryptUtil import *
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ntpath

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Homework by student:1100336", "This Homework made from student 1100336")
file_path = filedialog.askopenfilename( title='Plain text')
print(file_path)

PublicKeyPath = filedialog.askopenfilename( title='Public Key Path')
publicKey = readKeyFile(PublicKeyPath)

CipherFilePath = filedialog.asksaveasfile(initialfile = ntpath.basename(file_path)+".cipher")

# os.system("ls")

encrptoFile(file_path, CipherFilePath.name, publicKey)
