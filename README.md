# RSA-AES
RSA-AES Hybrid ecrypt by 蕭維均

# Enviroment requirement

## Ubuntu
Require PyCryptodome module
```
pip3 install -U PyCryptodome
```

## Windows

Require python3,MSVC v142 x64/x86 or MSVC v140 x64/x86

```
pip install pycryptodomex --no-binary :all:
pip install PyCryptodome
```

please read PyCryptodome official tutorial

[https://pycryptodome.readthedocs.io/en/latest/src/installation.html](https://pycryptodome.readthedocs.io/en/latest/src/installation.html)

# run

After you have the python eviroment and PyCryptodome,you can run it.

### 1.Get RSA key pair

```
python3 RSAKeyPair.py
```

### 2.Encrypt

```
python3 Encrypt.py
```

### 3.Decrypt

```
python3 Decrypt.py
```

# Download Binary

**Warning!!! if you run on Windows,Please try to using python script because Microsoft Defender will autoremove this binary version RSA-AES program**

[Ubuntu20.04](https://github.com/AlexTrinityBlock/RSA-AES/raw/master/Executable/Ubuntu20.04.zip)  
[Windows](https://github.com/AlexTrinityBlock/RSA-AES/raw/master/Executable/Windows_64bit.zip)
