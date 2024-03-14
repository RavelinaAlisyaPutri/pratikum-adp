# Program Python untuk menghitung rata-rata nilai mahasiswa
jumlah_mahasiswa = int(input('Masukkan jumlah mahasiswa: '))

for i in range(1, jumlah_mahasiswa + 1):
    print(f'Data Mahasiswa ke-{i}')
    
    nilai_tugas = float(input('Nilai Tugas: '))
    nilai_kuis = float(input('Nilai Kuis: '))
    nilai_uts = float(input('Nilai UTS: '))
    nilai_uas = float(input('Nilai UAS: '))
    nilai_keaktifan = float(input('Nilai Keaktifan: '))
   
    rata_rata = (nilai_tugas +  nilai_kuis + nilai_uts + nilai_uas + nilai_keaktifan)/5
    ragam = ((nilai_tugas-rata_rata)**2+(nilai_kuis-rata_rata)**2+(nilai_uts-rata_rata)**2+(nilai_uas-rata_rata)**2+(nilai_keaktifan-rata_rata)**2)/5
    simpangan_baku = ragam**(1/2)
    
    print(f'Rata-rata nilai mahasiswa ke-{i}: {rata_rata:.2f}\n')
    print(f'Ragam nilai mahasiswa ke-{i}: {ragam:.2f}\n')
    print(f'Simpangan baku nilai mahasiswa ke-{i}: {simpangan_baku:.2f}\n')