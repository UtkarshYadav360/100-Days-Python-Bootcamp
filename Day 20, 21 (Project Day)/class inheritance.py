# class inheritance
# using class inheritance we can use all the functionalities of other class in another class.


class Animal:
    def __init__(self):
        self.eyes = "2"

    def breathe(self):
        print("Inhale, Exhale")


elephant = Animal()
print(elephant.eyes)
elephant.breathe()


print()


# using the functionalities of "Animal" class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")

    def swim(self):
        print("Moves in water.")


salmon = Fish()
print(salmon.eyes)
salmon.breathe()
salmon.swim()
