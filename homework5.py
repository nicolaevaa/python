class Cat:
    def __init__(self, name, breed, weight, color):
        self._name = name
        self.breed = breed
        self.weight = weight
        self.color = color

    def hunt(self):
        return "I hunt mouses"

    def get_name(self):
        return f"Hello! I'm {self.__name}"

    def set_name(self, new_name):
        self.name = new_name


cat1 = Cat("Barsik", "thai", 5, "black-white")
print(cat1.name)
print(cat1.breed)
print(cat1.weight)
print(cat1.color)
print(cat1.get_name())



class Thai(Cat):
    def __init__(self, name, breed, weight, color, behavior):
        super().__init__(name, breed, weight, color)
        self.behavior = behavior


cat2 = Thai("Bars", "thai-siamese", 7, "white-black", "playful")
print(cat2._name)
print(cat2.breed)
print(cat2.weight)
print(cat2.color)
print(cat2.behavior)
print(cat2.hunt())
print(cat2.set_name('Barc'))
print(cat2.name)
print(cat2._name)

