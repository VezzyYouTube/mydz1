class Animal:
    def __init__(self, speed=20):
        self.speed = speed

dog = Animal()
wolf = Animal(speed=45)
print('SPEED')
print('dog:')
print(dog.speed)
print('wolf:')
print(wolf.speed)
print('=========')

class Animal:
    def __init__(self, satiety=50):
        self.satiety = satiety

dog = Animal()
wolf = Animal(satiety=75)
print('SATIETY')
print('dog:')
print(dog.satiety)
print('wolf:')
print(wolf.satiety)
print('*************')
print('*************')

class Auto:
    def __init__(self, speed=100):
        self.speed = speed

bmw = Auto()
mersedes = Auto(speed=125)
print('SPEED')
print('BMW:')
print(bmw.speed)
print('Mersedes:')
print(mersedes.speed)
print('=========')

class Auto:
    def __init__(self, fuel=25):
        self.fuel = fuel

bmw = Auto()
mersedes = Auto(fuel=30)
print('FUEL')
print('BMW:')
print(bmw.fuel)
print('Mersedes:')
print(mersedes.fuel)

