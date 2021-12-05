# pip3 uninstall PyCrypto
# pip3 install -U PyCryptodome
from Crypto import PublicKey
from usr.HomeWorkCryptUtil import *
import os



if __name__ == '__main__':
    print("Encrypt or Decrypt: (e/d)")
    optionChoice: str = input()

    if optionChoice == "e":
        print("Input the file name that you want to encrpto:")
        inputFile: str = input()
        print("Input the cipher file name:")
        cipherFile: str = input()
        publicKey = readKeyFile("./PublicKey/PublicKey")
        encrptoFile("./PlainText/"+inputFile, "./CipherText/"+cipherFile, publicKey)
    elif optionChoice == "d":
        privateKey=readKeyFile("./PrivateKey/PrivateKey")
        print("Input the cipher file name:")
        cipherFile: str = input()
        print("Input the decrypt file name:")
        decryptFile: str = input()
        decrptoFile("./CipherText/"+cipherFile, "./PlainText/"+decryptFile, privateKey)
        print("done")