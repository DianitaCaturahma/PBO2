'''Dianita Caturahma
210511147
Kelas D'''

class celcius:
    
    def __init__(self, celcius):
        self.celcius = celcius
        
    def kelvin(self):
        return (self.celcius + 273.15)
     
celciusE = celcius(80)
print(f"Celcius Ke Kelvin: {celciusE.kelvin()}")
