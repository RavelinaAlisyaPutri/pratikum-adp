import pygame
import random
import sys
import time

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Ukuran layar
lebar_layar = 400
tinggi_layar = 600

# Setup layar
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Flappy Box")

# Variabel game
box_x = 50
box_y = 300
ukuran_box = 30  # Ukuran persegi panjang
kecepatan_box = 0
percepatan_box = 0.5
box_flap = -8

lebar_pipa = 70
jarak_pipa = 150
pipa_x = lebar_layar
tinggi_pipa1 = random.randint(50, 400)
tinggi_pipa2 = tinggi_layar - tinggi_pipa1 - jarak_pipa
kecepatan_pipa = 3

score = 0
ukuran_score = pygame.font.Font(None, 36)

# Fungsi untuk menampilkan skor
def nilai_score():
    score_pemain = 'Score: ' + str(score)
    score_rendered = ukuran_score.render(score_pemain, True, WHITE)
    layar.blit(score_rendered, (10, 10))

# Fungsi untuk menampilkan pesan game over dan menyimpan skor
def game_over(player_name):
    # Simpan skor dan nama ke dalam file
    with open('score_pemain.txt', 'a') as file:
        file.write(player_name + ': ' + str(score))

    # Jeda sebelum keluar
    time.sleep(3)

    # Quit Pygame
    pygame.quit()
    sys.exit()

# Loop utama permainan
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                kecepatan_box = box_flap  # Melompat naik

    # Update box position
    kecepatan_box += percepatan_box
    box_y += kecepatan_box

    # Update pipe position
    pipa_x -= kecepatan_pipa
    if pipa_x < -lebar_pipa:
        pipa_x = lebar_layar
        tinggi_pipa1 = random.randint(50, 400)
        tinggi_pipa2 = tinggi_layar - tinggi_pipa1 - jarak_pipa
        score += 1

    # Tabrakan
    box_rect = pygame.Rect(box_x, box_y, ukuran_box, ukuran_box)
    pipa1_rect = pygame.Rect(pipa_x, 0, lebar_pipa, tinggi_pipa1)
    pipa2_rect = pygame.Rect(pipa_x, tinggi_pipa1 + jarak_pipa, lebar_pipa, tinggi_pipa2)
    if box_rect.colliderect(pipa1_rect) or box_rect.colliderect(pipa2_rect) or box_y > tinggi_layar:
        # Input nama pemain dari terminal
        player_name = input("Masukkan nama pemain: ")
        game_over(player_name)

    # Render
    layar.fill(BLUE)
    pygame.draw.rect(layar, WHITE, box_rect)  # Gambar persegi panjang untuk box
    pygame.draw.rect(layar, GREEN, pipa1_rect)  # Gambar pipa atas
    pygame.draw.rect(layar, GREEN, pipa2_rect)  # Gambar pipa bawah
    nilai_score()

    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
