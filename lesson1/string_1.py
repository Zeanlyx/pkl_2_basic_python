import os
from time import sleep

#clear layar terlebih dahulu 
os.system("clear") #cls

#tampilkan judul aplikasi
title    = """
===========================
 A P L I K A S I - B I J I 
===========================
"""
#tampilan
print(title)

#tunggu 3 detik
sleep(3)


username = input (" Masukan username: ")
sleep(2)
address  = input (" Masukan alamat: ")
sleep(2)
phone    = input (" Masukan phone: ")
sleep(2)
email    = input (" Masukan email: ")

text = f"""
----------------------------------------------------
      nama          : {username} 
----------------------------------------------------      
      alamat        : {address}
----------------------------------------------------      
      phone         : {phone}
----------------------------------------------------      
      email         : {email}
----------------------------------------------------     
"""
sleep(2)
os.system("clear")

print(text)