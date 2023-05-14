'''Dianita Caturahma 
210511147
kelas D'''

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}")

bukuA = Buku("Matahari", "Tere Liye")
bukuA.info()