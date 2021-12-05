from usr.HomeWorkCryptUtil import *
import os
from tkinter import filedialog

print("Generate RSA key pair")
publicKey, privateKey = RSAKeyPair()

PublicKeyPath = (filedialog.asksaveasfile(initialfile = "PublicKey")).name
PrivateKeyPath = (filedialog.asksaveasfile(initialfile = "PrivateKey")).name

if os.path.isfile(PublicKeyPath):os.system("rm "+PublicKeyPath)
if os.path.isfile(PrivateKeyPath):os.system("rm "+PrivateKeyPath)

writeByte(publicKey,PublicKeyPath)
writeByte(privateKey,PrivateKeyPath)