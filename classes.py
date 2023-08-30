
class Data:
    """A display of euler, golden ratio and pi numbers
    The self parameter is a reference to the current instance 
    of the class, 
    and is used to access variables that belongs to the class.
    """

    def __init__(self, euler_number, pi_number, golden_ratio):
        self.euler_number = euler_number
        self.pi_number = pi_number
        self.golden_ratio = golden_ratio
    
    def msg_function(self):
        print("The euler number is", self.euler_number)
        print("The golden ratio is", self.golden_ratio)
        print("The pi number is", self.pi_number)

#Instantiation of class data with object val
val = Data(2.718, 3.14, 1.618)
print(getattr(val,'euler_number'))
print(val.golden_ratio)
print(val.pi_number)
val.msg_function()

class kingdom:
    """Class that holds species and genus"""
    def __init__(self, genus, species):
        self.genus = genus
        self.species = species
 
    def microorganism(self):
        print(f'''The name of a microorganism is in the form of 
        {self.genus} {self.species}.''')

# Use the kingdom class to create an object, and then execute the microorganism method
animal = kingdom('Asspegillas', 'niger')
print(f'The genus is {animal.genus}, and the species is {animal.species}')
animal.microorganism()

# Create a Child Class in kingdom Class
class Recombinant(kingdom):
    def __init__(self, genus, species,activity):
        kingdom.__init__(self, genus, species)
        self.activity = activity  #This information was adedd as a Property

    def increment(self):
        print(f'''With this new recombinant {self.genus} {self.species} strain,\\\
the enzyme activity increased 2-times with {self.activity} U/ml''')

animal_1 = Recombinant('Aspergillus', 'sojae', 2500)
animal_1.microorganism()
animal_1.increment()

class Animal(object):
    """Illustrating inheritance using class animal and child class cow """
    def __init__(self, AnimalName):
        print(AnimalName, 'lives in a farm.')
 
class Cow(Animal):
    def __init__(self):
        print('Cow gives us milk.')
        "Using the super method"
        super().__init__('Cow')