import pygame
import random
import sys

import os
os.system("cls")

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
bird_x = 50
bird_y = 300
ukuran_bird = 30  # Ukuran persegi panjang
kecepatan_bird = 0
percepatan_bird = 0.5
bird_flap = -8

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
def game_over():
    # Tampilkan pesan game over
    game_over_text = ukuran_score.render('Game Over', True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(lebar_layar // 2, tinggi_layar // 2))
    layar.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.delay(2000)

    # Tanyakan nama pemain
    input_box = pygame.Rect(lebar_layar // 2 - 100, tinggi_layar // 2 + 50, 200, 32)
    player_name = ''
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        layar.fill(BLUE)
        pygame.draw.rect(layar, WHITE, input_box, 2)
        font = pygame.font.Font(None, 32)
        text_surface = font.render(player_name, True, WHITE)
        layar.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        input_box.w = max(200, text_surface.get_width() + 10)
        nilai_score()
        pygame.display.flip()

    # Simpan skor dan nama ke dalam file
    with open('score_pemain.txt', 'a') as file:
        file.write(f'{player_name}: {score}\n')

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
                kecepatan_bird = bird_flap  # Melompat naik

    # Update bird position
    kecepatan_bird += percepatan_bird
    bird_y += kecepatan_bird

    # Update pipe position
    pipa_x -= kecepatan_pipa
    if pipa_x < -lebar_pipa:
        pipa_x = lebar_layar
        tinggi_pipa1 = random.randint(50, 400)
        tinggi_pipa2 = tinggi_layar - tinggi_pipa1 - jarak_pipa
        score += 1

    # Tabrakan
    bird_rect = pygame.Rect(bird_x, bird_y, ukuran_bird, ukuran_bird)
    pipa1_rect = pygame.Rect(pipa_x, 0, lebar_pipa, tinggi_pipa1)
    pipa2_rect = pygame.Rect(pipa_x, tinggi_pipa1 + jarak_pipa, lebar_pipa, tinggi_pipa2)
    if bird_rect.colliderect(pipa1_rect) or bird_rect.colliderect(pipa2_rect) or bird_y > tinggi_layar:
        game_over()

    # Render
    layar.fill(BLUE)
    pygame.draw.rect(layar, WHITE, bird_rect)  # Gambar persegi panjang untuk burung
    pygame.draw.rect(layar, GREEN, pipa1_rect)  # Gambar pipa atas
    pygame.draw.rect(layar, GREEN, pipa2_rect)  # Gambar pipa bawah
    nilai_score()

    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
