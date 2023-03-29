'''Dianita Caturahma 
210511147
kelas D'''
 
class Celcius:
    def __init__ (self, celcius, fahrenheit, kelvin, reamur):
        self.celcius = celcius
        self.fahreheit = fahrenheit
        self.kelvin = kelvin
        self.reamur = reamur 

    def to_fahrenheit (self):
        return (9/5) * celcius + 32 
    
    def to_kelvin (self):
        return celcius + 273
    
    def info(self):
        print (f"konversi",Celcius. "derajat celcius adalah",fahrenheit, "derajat fahrenheit")

