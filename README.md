PRAKTIKUM 7

#penjelasan Program

1. Fungsi
hitung_nilai_akhir
Fungsi ini menerima tiga parameter: nilai_tugas, nilai_uts, dan nilai_uas.
Menghitung nilai akhir berdasarkan bobot:
30% dari nilai tugas.
35% dari nilai UTS.
35% dari nilai UAS.
Mengembalikan hasil perhitungan nilai akhir.


2. Dictionary data_mahasiswa
Berfungsi untuk menyimpan data mahasiswa dalam format NIM sebagai kunci.
Setiap NIM memiliki nilai berupa dictionary berisi:
nama: Nama mahasiswa.
nilai_tugas: Nilai tugas mahasiswa.
nilai_uts: Nilai UTS mahasiswa.
nilai_uas: Nilai UAS mahasiswa.
nilai_akhir: Nilai akhir mahasiswa.


3. Menu Utama
Program menggunakan loop utama untuk terus menampilkan menu hingga pengguna memilih opsi keluar (K).
Menu yang tersedia:

L (Lihat Data):
Menampilkan seluruh data mahasiswa dalam format tabel.

T (Tambah Data):
Meminta input nama, NIM, nilai tugas, UTS, dan UAS.
Menghitung nilai akhir menggunakan fungsi hitung_nilai_akhir.
Menyimpan data ke dalam dictionary data_mahasiswa.

U (Ubah Data):
Meminta NIM mahasiswa yang datanya ingin diubah.
Jika ditemukan, meminta input nilai baru dan memperbarui data.

H (Hapus Data):
Meminta NIM mahasiswa yang datanya ingin dihapus.
Menghapus data mahasiswa berdasarkan NIM jika ditemukan.

C (Cari Data):
Meminta NIM mahasiswa untuk dicari.
Menampilkan data jika ditemukan.

K (Keluar):
Mengakhiri program.


4. Validasi
Program memeriksa apakah NIM yang diinput ada dalam dictionary sebelum melakukan operasi (ubah, hapus, atau cari).
Jika data tidak ditemukan, pesan akan ditampilkan ke pengguna.

# Program

![Screenshot 2024-11-29 211118](https://github.com/user-attachments/assets/5a39682c-7a9c-4399-a592-66dbceb5a157)
![Screenshot 2024-11-29 211151](https://github.com/user-attachments/assets/79d7ade5-341a-4e02-a429-c42c1f3c6968)

# Hasil Program

![Screenshot 2024-11-29 211436](https://github.com/user-attachments/assets/f8c9eb44-acdd-4689-b307-1e074eaf86a6)
![Screenshot 2024-11-29 211512](https://github.com/user-attachments/assets/ac937c88-aa30-463c-88ec-fa929f328d6a)


# Flow Chart

![image](https://github.com/user-attachments/assets/44230cf6-d7aa-40a1-b964-f1dd43f5fbbf)



