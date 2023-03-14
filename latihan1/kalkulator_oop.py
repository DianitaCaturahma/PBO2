#Dianita Caturahma
class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
         return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
    
    # Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(4, 11)) # Output: 15
print(Kalkulator.subtract(20, 2)) # Output: 18

# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(5, 4)) # Output: 20
print(Kalkulator.divide(16, 4)) # Output: 4.0