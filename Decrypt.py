#!/usr/bin/python
# -*- coding: utf-8 -*-
from usr.HomeWorkCryptUtil import *
import os
import tkinter as tk
from tkinter import filedialog
import ntpath

root = tk.Tk()
root.withdraw()
cipherFilePath = filedialog.askopenfilename( title='Cipher text')
print(cipherFilePath)

PrivateKeyPath = filedialog.askopenfilename( title='Private Key Path ')
PrivateKey=readKeyFile(PrivateKeyPath)

PlainFilePath = filedialog.asksaveasfile(initialfile = (ntpath.basename(cipherFilePath)).replace(".cipher",""))
PlainFilePath = PlainFilePath.name
os.system("ls")

PlainFileName = ntpath.basename(cipherFilePath)
decrptoFile(cipherFilePath,PlainFilePath , PrivateKey)
print("done")
