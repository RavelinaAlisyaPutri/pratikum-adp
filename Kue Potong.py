import os
from termcolor import cprint

def kotak_kue():
    baris=13
    for j in range (baris):
        kue= [
            ("on_white", 32),
            ("on_white", 18, "on_red", 4, "on_white", 10),
            ("on_white", 16, "on_red", 2, "on_magenta", 2, "on_white", 2, "on_red", 2, "on_white", 8),
            ("on_white", 14, "on_magenta", 2, "on_red", 2, "on_magenta", 4, "on_red", 2, "on_white", 8),
            ("on_white", 10, "on_magenta", 4, "on_white", 4, "on_red", 4, "on_white", 2, "on_magenta", 2, "on_white", 6),
            ("on_white", 6, "on_magenta", 4, "on_white", 16, "on_magenta", 2, "on_white", 4),
            ("on_white", 4, "on_magenta", 24, "on_white", 4),
            ("on_white", 4, "on_magenta", 2, "on_light_red", 20, "on_magenta", 2, "on_white", 4),
            ("on_white", 4, "on_magenta", 2, "on_light_yellow", 20, "on_magenta", 2, "on_white", 4),
            ("on_white", 4, "on_magenta", 2, "on_light_red", 20, "on_magenta", 2, "on_white", 4),
            ("on_white", 4, "on_magenta", 2, "on_light_yellow", 20, "on_magenta", 2, "on_white", 4),
            ("on_white", 4, "on_magenta", 24, "on_white", 4),
            ("on_white", 32),
        ]
    
    for baris in kue:
        index = 0
        while index < len(baris):
            color = baris[index]
            lebar = baris[index + 1]
            cprint(' ' * lebar, 'black', color, end='')
            index += 2
        print()

if __name__ == "__main__":
    os.system('')  
    kotak_kue()
