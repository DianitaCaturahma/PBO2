class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def presentasi(self):
        print(self.nama, "presentasi")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")
class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang Bekerja Sebagai", self.pekerjaan)
mhs_pekerja = MahasiswaPekerja("Dianita", "210511147", "UI Designer")
mhs_pekerja.presentasi() 
mhs_pekerja.bekerja() 
mhs_pekerja.bersosialisasi() 