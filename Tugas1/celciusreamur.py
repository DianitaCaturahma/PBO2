'''Dianita Caturahma
210511147
Kelas D'''

class celcius:
    
    def __init__(self, celcius):
        self.celcius = celcius
        
    def reamur(self):
        return (self.celcius * 4/5)
     
celciusE = celcius(77)

print(f"Celcius Ke Kelvin: {celciusE.reamur()}")
