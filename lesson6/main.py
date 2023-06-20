#perulangan atau mengulang program 

# from os import system
# from anyio import sleep


# # kegiatan = ["game", "music", "ngoding", "tidur", "nyantuy", "repeat"]

# # # for item in kegiatan:
# # #     print(item)

# # # phoneNumber = ["129749137", "2194719431", "92130712090", "10248112498", "12401024209", "2141253412"]

# for item in phoneNumber:
#     # print(f"whatsapp terkirim ke : {item}")
#     file = open(f"{item}.txt", "w")  
#     file.write(item)
#     sleep(2)

#membuat spam 
# for item in range(10):
#     system("open ")
#     sleep(2)


import webbrowser

def buka_url():
    webbrowser.open("https://youtube.com/")
        
buka_url("https://youtube.com/")