program PembelianTiketPesawat;

var
  nama, jenis_kelamin : string;
  umur, tujuan, maskapai, harga_tiket, jumlah_tiket : integer;
  total_harga : Real ;
 

begin
  writeln('PEMESANAN TIKET PESAWAT RA AIR');
  write('Nama pemesan: ');
  readln(nama);
  write('Umur: ');
  readln(umur);
  write('Jenis kelamin (Perempuan/Laki-laki): ');
  readln(jenis_kelamin);
  writeln('Pilih tujuan: ');
  writeln('1. Zimbabwe');
  writeln('2. Paris');
  writeln('3. Italia');
  write('Tujuan penerbangan: ');
  readln(tujuan);
  
  writeln;
  
  writeln('Pilih maskapai:');
  writeln('1. Ekonomi - Rp 3.000.000');
  writeln('2. Bisnis - Rp 4.500.000');
  writeln('3. First Class - Rp 7.300.000');
  write('Kelas maskapai: ');
  readln(maskapai);
  if maskapai = 1 then
    harga_tiket := 3000000
  else if maskapai = 2 then
    harga_tiket := 4500000
  else
    harga_tiket := 7300000;
    
  write('Jumlah pemesanan tiket: ');
  readln(jumlah_tiket);
  total_harga := harga_tiket * jumlah_tiket;
  if jumlah_tiket > 3 then
    total_harga := total_harga * 0.75 ;
  
  writeln;
  
  writeln('--- Struk Pemesanan Tiket Pesawat ---');
  writeln('Nama: ', nama);
  writeln('Umur: ', umur);
  writeln('Jenis Kelamin: ', jenis_kelamin);
  writeln('===============================');
  writeln('Negara Tujuan: ', tujuan);
  writeln('Jenis Maskapai: ', maskapai);
  writeln('Jumlah Tiket: ', jumlah_tiket);
  writeln('Total Harga: Rp', total_harga);
end.
