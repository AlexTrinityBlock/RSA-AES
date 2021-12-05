from usr.HomeWorkCryptUtil import *
import os
import tkinter as tk
from tkinter import filedialog
import ntpath

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename( title='Plain text')
print(file_path)

PublicKeyPath = filedialog.askopenfilename( title='Public Key Path')
publicKey = readKeyFile(PublicKeyPath)

CipherFilePath = filedialog.asksaveasfile(initialfile = ntpath.basename(file_path)+".cipher")

os.system("ls")

encrptoFile(file_path, CipherFilePath.name, publicKey)
