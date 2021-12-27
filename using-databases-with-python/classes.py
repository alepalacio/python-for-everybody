class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far',self.x)

an = PartyAnimal()

print(an)
print(type(an))
print(dir(an))

"""
Constructors and destructors.
"""

class PartyAnimal:
    x = 0
    
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed',self.x)

an = PartyAnimal()
print(an.party())
print(an.party())
print(an)

"""
Third example
"""

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
print(s.party())

j = PartyAnimal("Jim")
print(j.party())