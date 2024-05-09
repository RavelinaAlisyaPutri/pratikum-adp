produk = [
    ["Civic", 22700, 21],
    ["Lexus", 42500, 9],
    ["Audi", 74400, 17],
    ["Porsche", 98750, 5]
]

print("Tabel Harga dan Stok Barang:")
print("+--------------+------------+------+")
print("| Nama Produk  | Harga(US$) | Stok |")
print("+--------------+------------+------+")
for item in produk:
    print(f"| {item[0]:12} | {item[1]:10} | {item[2]:4} |")
print("+--------------+------------+------+")

laba_produk = []
for item in produk:
    keuntungan = item[1] * item[2]
    laba_produk.append([item[0], keuntungan])

for i in range(len(laba_produk)):
    for j in range(i + 1, len(laba_produk)):
        if laba_produk[i][1] > laba_produk[j][1]:
            laba_produk[i], laba_produk[j] = laba_produk[j], laba_produk[i]
laba_max = laba_produk[-1][0]
laba_min = laba_produk[0][0]

total_laba = 0
for item in laba_produk:
    total_laba += item[1]
total_laba = format(total_laba)

print(f"Produk dengan Keuntungan Terbesar: {laba_max}")
print(f"Produk dengan Keuntungan Terkecil: {laba_min}")
print(f"Total Keuntungan: {total_laba}")
    