# MEMBUAT APLIKASI UNDAGAN SEDERHANA
import os


def listUndangan():
    print("""
___  ___  ___   _   _ _____ ___  ______ 
|  \/  | / _ \ | \ | |_   _/ _ \ | ___ \
| .  . |/ /_\ \|  \| | | |/ /_\ \| |_/ /
| |\/| ||  _  || . ` | | ||  _  ||  __/ 
| |  | || | | || |\  | | || | | || |    
\_|  |_/\_| |_/\_| \_/ \_/\_| |_/\_| 
""")
    fileData = open("database.txt", "a")
    nama = input("masukan Nama :")
    alamat = input("masukan Alamat :")
    phone = input("masukan nomor telepon :")
    age = input("Masukan umur :")

    formatText = f"{nama},{alamat},{phone},{age}\n"
    
    fileData.write(formatText)

def readUndangan():
    fileData = open("database.txt", "r")
    result = fileData.read()
    os.system("clear")
    print(result)
    
listUndangan()
readUndangan()
