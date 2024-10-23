class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print('Inhale, Exhale!  ')


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.size = 20

    def swim(self):
        print('swinmming!')


fish = Fish()

fish.breath()
fish.swim()