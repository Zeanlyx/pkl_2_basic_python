#flow

def cekusia(usia):
    #jika usia di bawah 20 maka jangan izinkan
    if usia < 20:
        print("Kamu Belum Bisa Masuk")
    else :
        print("Silahkan Masuk")


def CheckUsername():
    username = input("Masukan username : ")
    if  username == "mahesa":
            print("Login Berhasil")
    else :
        print("Username Tidak Terdafatar!")
        

def Login():
    username = input("Masukan Username :")
    password = input("Masukan Password :")
    
    if username == "mahesa" and password == "1124":
        print("Login Berhasil")
    else :
        print("Login GAGAL !")

def Login2():
    username = input("Masukan Username :")
    password = input("Masukan Password :")

    if username != "mahesa" or password !="1124":
        print("USERNAME ATAU PASSWORD SALAH !") 
        return
        
        print("SELAMAT DATANG !")

def Login3():
    DataUsername = ["mahesa", "najwa"]
    DataPassword = ["123", "221"]
    
    username = input("Masukan Username :")
    
    if username not in DataUsername:
        print("Username Tidak di Temukan !")
        return
    password = input("Masukan Password :")
    
    if password not in DataPassword:
        print("Password SALAH !")
        return
    print("""
===============================
   S E L A M A T D A T A N G ! 
===============================         
          """)

Login3()
