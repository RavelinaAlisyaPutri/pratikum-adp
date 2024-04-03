kelipatan_DOR = 0

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print("{:<4}".format("DOR"), end="")
        kelipatan_DOR += 1
    else:
        print("{:<4}".format(i), end="")
    
    if i % 10 == 0:
        print()

print(f"\nTotal 'DOR' yang muncul adalah" ,kelipatan_DOR, "kali.")