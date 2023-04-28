class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "Terbang")
class burung(Hewan):
    def __init__(self, nama, umur, jenis_burung):
        super().__init__(nama, umur)
        self.jenis_burung = jenis_burung
    def bersuara(self):
        print("kukkkukkk!!!!")
burungA = burung("Burung", 2, "Merpati")
burungA.bergerak() # output: Burung Terbang
burungA.bersuara() # output: kukkkukkk!!!!