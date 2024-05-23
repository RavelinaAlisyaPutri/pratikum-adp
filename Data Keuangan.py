import json

# Menu utama program
def menu_utama():
    data_keuangan = muat_data()
    while True:
        print("\nMenu:")
        print("1. Tampilkan Data Keuangan")
        print("2. Tambah Transaksi Baru")
        print("3. Hapus Transaksi")
        print("4. Tampilkan Total Uang")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            tampilkan_data(data_keuangan)
        elif pilihan == '2':
            tambah_transaksi(data_keuangan)
        elif pilihan == '3':
            hapus_transaksi(data_keuangan)
        elif pilihan == '4':
            tampilkan_total(data_keuangan)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")
            
# Menampilkan data keuangan
def tampilkan_data(data_keuangan):
    print("Tanggal\t\tKeterangan\tJumlah\t\tTipe")
    for transaksi in data_keuangan:
        tipe_transaksi = "Pengeluaran" if transaksi['tipe'] == 'A' else "Pemasukan"
        print(f"{transaksi['tanggal']}\t{transaksi['keterangan']}\t{transaksi['jumlah']}\t{tipe_transaksi}")

# Menambah transaksi baru
def tambah_transaksi(data_keuangan):
    tanggal = input("Tanggal transaksi: ")
    keterangan = input("Keterangan transaksi: ")
    jumlah = int(input("Jumlah transaksi: "))
    print("Tipe:\nA. Pengeluaran\nB. Pemasukan")
    tipe = input("Tipe transaksi (A/B): ")
    data_keuangan.append({"tanggal": tanggal, "keterangan": keterangan, "jumlah": jumlah, "tipe": tipe})
    simpan_data(data_keuangan)

# Menghapus transaksi
def hapus_transaksi(data_keuangan):
    tampilkan_data(data_keuangan)
    index = int(input("Masukkan index transaksi yang ingin dihapus: "))
    if 0 <= index < len(data_keuangan):
        del data_keuangan[index]
        simpan_data(data_keuangan)  
        print("Transaksi berhasil dihapus.")
    else:
        print("Index transaksi tidak valid.")

# Menyimpan data ke file teks
def simpan_data(data_keuangan):
    with open('data_keuangan.txt', 'w') as file:
        file.write(json.dumps(data_keuangan))

# Memuat data dari file teks
def muat_data():
    try:
        with open('data_keuangan.txt', 'r') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return []

# Menampilkan total uang
def tampilkan_total(data_keuangan):
    total_pemasukan = sum(transaksi['jumlah'] for transaksi in data_keuangan if transaksi['tipe'] == 'B')
    total_pengeluaran = sum(transaksi['jumlah'] for transaksi in data_keuangan if transaksi['tipe'] == 'A')
    print(f"Total Pemasukan: {total_pemasukan}")
    print(f"Total Pengeluaran: {total_pengeluaran}")
    print(f"Total Uang: {total_pemasukan - total_pengeluaran}")

# Jalankan program
if __name__ == "__main__":
    menu_utama()
