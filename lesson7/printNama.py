def printNama(nama):
    print(nama)
    print("zeanlyx")

def cekUmur(usia):
    
    if usia < 20:
            print("Umur anda di bawah ketentuan  ")
    else:
            print("kamu boleh masuk ")      
import hashlib
def Menu():
    print("""
          
      /$$$$$$  /$$      /$$  /$$$$$$   /$$$$$$ 
     /$$__  $$| $$  /$ | $$ /$$__  $$ /$$__  $$
    | $$  \ $$| $$ /$$$| $$| $$  \ $$| $$  \ $$
    | $$$$$$$$| $$/$$ $$ $$| $$$$$$$$| $$$$$$$$
    | $$__  $$| $$$$_  $$$$| $$__  $$| $$__  $$
    | $$  | $$| $$$/ \  $$$| $$  | $$| $$  | $$
    | $$  | $$| $$/   \  $$| $$  | $$| $$  | $$
    |__/  |__/|__/     \__/|__/  |__/|__/  |__/
                                                                                                                               
          """)
    print("""
===============================================================
      Menu  :      1.Login    2.Register     3.Exit          
===============================================================        
    """)

    menu = input("Masukan Menu :")

    if menu == "1" :
        print("Login")
        return
    
    if menu == "2":
        print("Register")
        return
    
    if menu == "3":
        print("TERIMAKASIH! ")
        exit()

Menu()
