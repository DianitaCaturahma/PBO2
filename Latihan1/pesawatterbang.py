'''Dianita Caturahma 
210511147
kelas D'''

class PesawatTerbang:
    def __init__(self, maskapai, tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan

    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")
    
pesawatA = PesawatTerbang("Air Asia", "Sabang - Merauke")
pesawatA.info()