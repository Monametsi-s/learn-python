class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is saying woof")
    
    def celebrate_birthday(self):
        print(f"{self.name} is turning {self.age} years old")
        
dog1 = Dog("Barbi", 5)
dog2 = Dog("Seyi", 3)

dog1.bark()
dog2.celebrate_birthday()