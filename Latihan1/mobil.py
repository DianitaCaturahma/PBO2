'''Dianita Caturahma 
210511147
kelas D'''

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

mobilA = Mobil("Mitsubishi", "Merah")
mobilA.info() # Output: Mobil Mitsubishi berwarna Merah