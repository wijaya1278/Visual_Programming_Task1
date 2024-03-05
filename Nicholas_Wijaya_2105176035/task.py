class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def display_info(self):
        print("Nama         : ", self.nama)
        print("Kelas        : ", self.kelas)
        print("Prodi        : ", self.prodi)
        print("Fakultas     : ", self.fakultas)
        print("Tempat Tinggal: ", self.tempat_tinggal)
        print("Asal         : ", self.asal)

# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa("Nicholas Wijaya", "2021 B", "Pendidikan Komputer", "FKIP", "Samarinda", "Samarinda")

    # Menampilkan informasi mahasiswa
    mahasiswa1.display_info()

