from random import randint

class Animal:
    def getHealth(self):
        return 'Sano' if self.weight >= self.wLimit else 'Enfermo'

class Venado(Animal):
    def __init__(self, id_, weight):
        self.id_ = id_
        self.weight = weight
        self.wLimit = 120

    def __str__(self):
        return 'Venado'

class Puma(Animal):
    def __init__(self, id_, weight, age):
        Venado.__init__(self, id_, weight)
        self.age = age
        self.wLimit = 200

    def getAge(self):
        return 'Adulto' if self.age >= 5 else 'Menor'

    def __str__(self):
        return 'Puma'

class Jaula:
    def __init__(self, animal_type, amount):
        self.animal_type = animal_type
        self.amount = amount

        if animal_type == Puma:
            self.animals = [animal_type(animal, randint(160, 260), randint(1, 10)) for animal in range(1, amount+1)]
        else:
            self.animals = [animal_type(animal, randint(80, 180)) for animal in range(1, amount+1)]

    def getAnimals(self):
        output = f'Jaula de {self.animals[0]}s'
        for animal in self.animals:
            output += f'\n# {animal.id_} - {animal.getHealth()}'
        return output

    def getAdults(self):
        if self.animal_type == Puma:
            adults = [animal.getAge() for animal in self.animals]
            return f'Cantidad de adultos {adults.count("Adulto")}'
        else:
            return 'Type of animal is not puma'

jaula1 = Jaula(Puma, 4)
print(jaula1.getAnimals())
print(jaula1.getAdults())

jaula1 = Jaula(Venado, 2)
print(jaula1.getAnimals())
print(jaula1.getAdults())
