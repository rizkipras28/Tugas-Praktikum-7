# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    return (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

while True:  # Loop utama program
    print("\nMenu:")
    print("L. Lihat Data")
    print("T. Tambah Data")
    print("U. Ubah Data")
    print("H. Hapus Data")
    print("C. Cari Data")
    print("K. Keluar")

    pilihan = input("Pilih menu (L/T/U/H/C/K):").upper()

    if pilihan == 'T':  # Tambah Data
        nama = input("Nama: ")
        nim = input("NIM: ")
        nilai_tugas = float(input("Nilai Tugas:"))
        nilai_uts = float(input("Nilai UTS:"))
        nilai_uas = float(input("Nilai UAS:"))

        nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

        # Simpan data ke dalam dictionary
        data_mahasiswa[nim] = {
            'nama': nama,
            'nilai_tugas': nilai_tugas,
            'nilai_uts': nilai_uts,
            'nilai_uas': nilai_uas,
            'nilai_akhir': round(nilai_akhir, 2)
        }
        print("Data berhasil ditambahkan.")

    elif pilihan == 'U':  # Ubah Data
        nim = input("Masukkan NIM mahasiswa yang ingin diubah:")
        if nim in data_mahasiswa:
            print("Data ditemukan. Silakan ubah data:")
            nilai_tugas = float(input("Nilai Tugas baru:"))
            nilai_uts = float(input("Nilai UTS baru:"))
            nilai_uas = float(input("Nilai UAS baru:"))

            nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

            # Update Data
            data_mahasiswa[nim].update({
                'nilai_tugas': nilai_tugas,
                'nilai_uts': nilai_uts,
                'nilai_uas': nilai_uas,
                'nilai_akhir': round(nilai_akhir, 2)
            })
            print("Data berhasil diubah.")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == 'H':  # Hapus Data
        nim = input("Masukkan NIM mahasiswa yang ingin dihapus:")
        if nim in data_mahasiswa:
            del data_mahasiswa[nim]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == 'L':  # Lihat Data
        print("\nDaftar Mahasiswa:")
        print(f"{'NIM':<10} {'Nama':<20} {'Tugas':<6} {'UTS':<6} {'UAS':<6} {'Akhir':<6}")
        for nim, info in data_mahasiswa.items():
            print(f"{nim:<10} {info['nama']:<20} {info['nilai_tugas']:<6}"
                  f"{info['nilai_uts']:<6} {info['nilai_uas']:<6} {info['nilai_akhir']:<6}")

    elif pilihan == 'C':  # Cari Data
        nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
        if nim in data_mahasiswa:
            info = data_mahasiswa[nim]
            print(f"Data ditemukan: {info['nama']}, Tugas: {info['nilai_tugas']}, UTS: {info['nilai_uts']}, UAS: {info['nilai_uas']}, Akhir: {info['nilai_akhir']}")
        else:
            print("Data tidak ditemukan.")

    elif pilihan == 'K':  # Keluar
        print("Program Selesai.")
        break  # Keluar dari loop

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
