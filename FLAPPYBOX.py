import pygame
import random
import sys
import time

import os
os.system ('cls')

# Warna
colors = [
    [255, 255, 255],  # WHITE
    [0, 0, 0],        # BLACK
    [0, 0, 255],      # BLUE
    [0, 255, 0],      # GREEN
]

# Ukuran layar
ukuran_layar = [400, 600]

# Inisiasi Pygame
pygame.init()

# Setup layar
layar = pygame.display.set_mode((ukuran_layar[0], ukuran_layar[1]))
pygame.display.set_caption("Flappy Box")

# Variabel game
box_x = 50
box_y = 300
ukuran_box = 30
kecepatan_box = 0
percepatan_box = 0.5
box_flap = -8

lebar_pipa = 70
jarak_pipa = 150
pipa_x = ukuran_layar[0]
tinggi_pipa1 = random.randint(50, 400)
tinggi_pipa2 = ukuran_layar[1] - tinggi_pipa1 - jarak_pipa
kecepatan_pipa = 3

score = 0
ukuran_score = pygame.font.Font(None, 36)

# Score Pemain
def nilai_score():
    score_pemain = 'Score: ' + str(score)
    score_hasil = ukuran_score.render(score_pemain, True, colors[0])
    layar.blit(score_hasil, (10, 10))

# game over dan menyimpan skor
def game_over(player_name):
    # Simpan score
    with open('score_pemain.txt', 'a') as file:
        file.write(player_name + ': ' + str(score) + '\n')

    # Jeda sebelum keluar
    time.sleep(3)

    # Keluar Pygame
    pygame.quit()
    sys.exit()

# Loop utama permainan
running = True
while running:
    # Proses gerak
    for loncat in pygame.event.get():
        if loncat.type == pygame.QUIT:
            running = False
        elif loncat.type == pygame.KEYDOWN:
            if loncat.key == pygame.K_SPACE:
                kecepatan_box = box_flap  # kotak melompat

    # Posisi box
    kecepatan_box += percepatan_box
    box_y += kecepatan_box

    # Posisi pipa
    pipa_x -= kecepatan_pipa
    if pipa_x < -lebar_pipa:
        pipa_x = ukuran_layar[0]
        tinggi_pipa1 = random.randint(50, 400)
        tinggi_pipa2 = ukuran_layar[1] - tinggi_pipa1 - jarak_pipa
        score += 1

    # Tabrakan
    if (
        box_x < pipa_x + lebar_pipa
        and box_x + ukuran_box > pipa_x
        and (box_y < tinggi_pipa1 or box_y + ukuran_box > tinggi_pipa1 + jarak_pipa)
    ):
        # Input nama pemain dari terminal
        player_name = input("Nama pemain: ")
        game_over(player_name)

    # Tampilan
    layar.fill(colors[2])  # BLUE
    pygame.draw.rect(layar, colors[0], (box_x, box_y, ukuran_box, ukuran_box))  # Gambar box
    pygame.draw.rect(layar, colors[3], (pipa_x, 0, lebar_pipa, tinggi_pipa1))  # Gambar pipa atas
    pygame.draw.rect(layar, colors[3], (pipa_x, tinggi_pipa1 + jarak_pipa, lebar_pipa, tinggi_pipa2))  # Gambar pipa bawah
    nilai_score()

    pygame.display.flip()

    # FPS game
    pygame.time.Clock().tick(60)

# Keluar Pygame
pygame.quit()
