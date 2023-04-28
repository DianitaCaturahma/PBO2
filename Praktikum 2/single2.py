class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang Olahraga.")
class mahasiswa(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim= nim
    def menjelaskan(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang memainkan Bola Basket.")
mahasiswaA = mahasiswa("Dianita", 35, "210511147")
mahasiswaA.berbicara() # Output: Dianita sedang Olahraga.
mahasiswaA.menjelaskan() # Output: Dianita dengan NIM 210511147 sedang memainkan Bola Basket..