#Блок задания 2:
#Создайте класс "Животное", который содержит информацию о виде и возрасте животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
#"Животное" и содержат информацию о породе.

class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

if __name__ == "__main__":
    dog = Dog("Собака", 3, "Лабрадор")
    cat = Cat("Кошка", 5, "Британская")
    
    print(f"Собака: {dog.species}, Возраст: {dog.age}, Порода: {dog.breed}")
    print(f"Кошка: {cat.species}, Возраст: {cat.age}, Порода: {cat.breed}")