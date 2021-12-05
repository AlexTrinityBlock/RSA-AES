from usr.HomeWorkCryptUtil import *
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()
messagebox.showinfo("Homework by student:1100336", "This Homework made from student 1100336")
messagebox.showinfo("Generate RSA key pair", "Generate RSA key pair")
print("Generate RSA key pair")
publicKey, privateKey = RSAKeyPair()

PublicKeyPath = (filedialog.asksaveasfile(initialfile = "PublicKey")).name
PrivateKeyPath = (filedialog.asksaveasfile(initialfile = "PrivateKey")).name

if os.path.isfile(PublicKeyPath):os.remove(PublicKeyPath)
if os.path.isfile(PrivateKeyPath):os.remove(PrivateKeyPath)

writeByte(publicKey,PublicKeyPath)
writeByte(privateKey,PrivateKeyPath)