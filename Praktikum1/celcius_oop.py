'''Dianita Caturahma
210511147
Kelas D'''

class Celcius: 
    @staticmethod 
    def to_fahrenheit(celsius): 
        return (celsius * 9/5) + 32 
     
    @staticmethod 
    def to_kelvin(celsius): 
        return celsius + 273.15 
     
    @staticmethod 
    def to_reamur(celsius): 
        return celsius * 4/5 
 
mycelcius = 50
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
mykelvin = Celcius.to_kelvin(mycelcius)
myreamur = Celcius.to_reamur(mycelcius) 
print(myfahrenheit)
print(mykelvin)
print(myreamur)
