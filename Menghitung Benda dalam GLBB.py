def hitung_glbb(kecepatan_awal, percepatan, waktu):
    kecepatan_akhir = kecepatan_awal + percepatan * waktu
    jarak =(kecepatan_awal * waktu + 0.5 * percepatan * waktu**2)/1000
    return kecepatan_akhir, jarak

n = int(input("Masukkan jumlah data: "))
data = []

for i in range(n):
    print(f"Data {i+1}")
    v0 = float(input("Kecepatan awal: "))
    a = float(input("Percepatan: "))
    t = float(input("Waktu: "))
    data.append((v0, a, t))

print("\nTabel Hasil Perhitungan GLBB:")
print("+----------------+-------------+-------+-----------------+-----------+")
print("| Kecepatan Awal | Percepatan  | Waktu | Kecepatan Akhir |   jarak   |")
print("|      (m/s)     |   (m/s^2)   |  (s)  |      (m/s)      |    (km)   |")
print("+----------------+-------------+-------+-----------------+-----------+")
for (v0, a, t) in data:
    v_akhir, s = hitung_glbb(v0, a, t)
    print(f"| {v0:<14.2f} | {a:<11.2f} | {t:<5.2f} | {v_akhir:<15.2f} | {s:<9.2f} |")
print("+----------------+-------------+-------+-----------------+-----------+")