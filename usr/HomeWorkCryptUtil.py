# pip3 uninstall PyCrypto
# pip3 install -U PyCryptodome
from ast import Str
from codecs import utf_16_be_decode
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util import Counter
from Crypto.PublicKey import RSA
import hashlib
import os
import string
import random


def randomAESKey():
    lst = [random.choice(string.ascii_letters + string.digits)
           for n in range(32)]
    s: str = "".join(lst)
    return s


def hash256(KeyStr: Str):
    byteString = bytes(KeyStr, "utf-8")
    hashObj = hashlib.sha256()
    hashObj.update(byteString)
    return hashObj.digest()


def encrptoBytes(plaintextBytes, key):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    return cipher.encrypt(plaintextBytes)


def decrptoBytes(ciphertextBytes, key):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    return cipher.decrypt(ciphertextBytes)


def writeByte(byteMsg, fileName):
    with open(fileName, "ab+") as f:
        f.write(byteMsg)


def readKeyFile(fileName):
    key = open(fileName, "rb").read()
    return key


def encrptoFile(InputFileName, outputFileName, RSAPublicKey):
    if os.path.isfile(outputFileName):
        os.system("rm "+outputFileName)
    # AES
    key = hash256(randomAESKey())
    print("AES key in crpto", key, "\n")
    cipherAESkey = RSAencrypto(key, RSAPublicKey)
    print("Cipher AES key in crpto:")
    print(cipherAESkey, "\n")
    writeByte(cipherAESkey, outputFileName)
    # AES
    with open(InputFileName, "rb") as f:
        fBytes = f.read(128)
        writeByte(encrptoBytes(fBytes, key), outputFileName)
        while fBytes:
            fBytes = f.read(128)
            writeByte(encrptoBytes(fBytes, key), outputFileName)


def decrptoFile(InputFileName, outputFileName, RSAPrivateKey):
    if os.path.isfile(outputFileName):
        os.system("rm "+outputFileName)
    print(InputFileName,RSAPrivateKey)
    key = RSAdecrypto(readCipherAESkey(InputFileName), RSAPrivateKey)
    print("AES key recover:", key, "\n")
    with open(InputFileName, "rb") as f:
        f.seek(256, 1)
        bytes = f.read(128)
        print(bytes)
        writeByte(decrptoBytes(bytes, key), outputFileName)
        while bytes:
            bytes = f.read(128)
            writeByte(decrptoBytes(bytes, key), outputFileName)


def RSAKeyPair():
    key = RSA.generate(2048)
    privateKey = key.exportKey()
    publicKey = key.publickey().exportKey()
    keyPair: list = [publicKey, privateKey]
    return keyPair


def RSAencrypto(AESkey: bytes, publicKey: bytes):
    cipherRSA = PKCS1_OAEP.new(RSA.importKey(publicKey))
    cipherAESkey = cipherRSA.encrypt(AESkey)
    return cipherAESkey


def RSAdecrypto(cipherAESkey: bytes, privateKey: bytes):
    cipherRSA = PKCS1_OAEP.new(RSA.importKey(privateKey))
    AESkey = cipherRSA.decrypt(cipherAESkey)
    return AESkey


def readCipherAESkey(InputFileName):
    with open(InputFileName, "rb") as f:
        bytes = f.read(256)
        return bytes

