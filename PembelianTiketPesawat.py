#Pembelian Tiket Pesawat
print('DATA PEMBELIAN TIKET RA AIR')
print()

nama = input('Nama pemesan: ')
umur = int(input('Umur: '))
jenis_kelamin = input('Jenis kelamin (P/L): ')

print('Pilih tujuan: ')   
print('1. Zimbabwe') 
print('2. Paris')
print('3. Italia')
tujuan = int(input('Tujuan penerbangan: '))

print()

print('Pilih maskapai:')
print('1. Ekonomi - Rp 3.000.000')
print('2. Bisnis - Rp 4.500.000')
print('3. First Class - Rp 7.300.000')
maskapai = int(input('Kelas maskapai: '))

if maskapai == 1 :
   harga_tiket = 3000000
elif maskapai == 2 :
   harga_tiket = 4500000
else :
   harga_tiket = 7300000
   
jumlah_tiket = int(input('Jumlah pemesanan tiket: '))
total_harga = harga_tiket * jumlah_tiket
if jumlah_tiket > 3:
   total_harga = total_harga*0.75  

print()

print('--- Struk Pemesanan Tiket Pesawat ---')
print('Nama: ', nama)
print('Umur: ' , umur)
print('Jenis Kelamin: ', jenis_kelamin)
print('===============================')
print('Negara Tujuan: ', tujuan)
print('Jenis Maskapai: ', maskapai)
print('Jumlah Tiket: ', jumlah_tiket)
print('Total Harga: Rp', str(total_harga))