from cryptography.fernet import Fernet

def keychk():
    import existance
    if existance.exists("universal.key") == "FALSE":
        key = Fernet.generate_key()
        with open("universal.key", "wb") as key_files:
            key_files.write(key)


def loadKey():
    key = open("universal.key","rb").read()
    return key

def Encrypt(secret):
    key = loadKey()
    encodeSecret = secret.encode()
    fer = Fernet(key)
    return fer.encrypt(encodeSecret)

def Decrypt(encryptSecret):
    key = loadKey()
    fer = Fernet(key)
    decryptSecret = fer.decrypt(encryptSecret)
    return decryptSecret.decode()