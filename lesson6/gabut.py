import pygame
import sys

#inisialisasi pygame
pygame.init()

#mengatur lebar dan tinggi layar
width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_mode((width, height))
pygame.display.set_caption('Gabut gw bangg')

#mengatur warna latar belakang 
background_color = (255, 255, 255)

#mengatur warna object
object_color = (255, 0, 0)

#mengatur posisi awal object
x, y = 50, 50

#mengatur kecepatan objek
vel_x, vel_y = 5, 5

clock = pygame.time.Clock()

#loop utama
while True:
    clock.tick(60) #batasi kecepatan frame ke 60 fps
    
    #periksa semua event yang terjadi 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #perbarui posisi objek
    x += vel_x
    x += vel_y
    
    #periksa jika objek mencapai batas layar
    if x <= 0 or x >= width:
        vel_x = -vel_x
    if y <= 0 or y >= height:
        vel_y = -vel_y
        
    #bersihkan layar
    screen.fill(background_color)
    
    #gambar objek dengan posisi yang baru 
    pygame.draw.circle(screen, object_color, (x, y), 30)
    
    #tampilkan gambar yang telah diperbarui pada layar
    pygame.display.flip()