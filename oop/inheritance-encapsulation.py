class Guitar:
    def __init__(self, n_strings=6):  # default value to be passed in init
        self.n_strings = n_strings
        self.play()  # it will automatically call this method whenever an instance is initialized

    def play(self):
        if self.n_strings == 6:
            print("6-string melody playing")
        elif self.n_strings > 6:
            print("loud melody rocking".upper())
        else:
            print("Non 6-string melody")

    def details(self):
        print(f'This is a {self.n_strings} guitar')


class ElectricGuitar(Guitar):
    def __init__(self):
        super().__init__(n_strings=8)  # we can passe the value in the init for a new value in class
        self.color = ("#000000", "#FFFFFF")  # black and white in hex, specializing the class
        self.__cost = 50  # __ before a attribute or namespace in general means it is "private"


class BassGuitar(Guitar):
    def __init__(self):
        super().__init__(n_strings=4)  # it will first initialize attributes and methods biased by that parent class

    def __make_6_strings(self):
        self.n_strings = 6


if __name__ == '__main__':
    my_guitar = Guitar()
    print("There are", my_guitar.n_strings, "strings on this guitar")
    # my_guitar.play()
    print("\nJust got my bass guitar: ")
    my_bass = BassGuitar()
    my_bass.details()

    print("\nJust got an 8-stringed guitar:")
    my_8_strings = ElectricGuitar()

    print("\nPrivate attributes may be accessed in Python: ")
    print(my_8_strings._ElectricGuitar__cost)  # and this is the way to do: with an underscore before the class

    print("\nLet's change our Bass number of strings using a 'private' method:")
    print(my_bass.details())
    my_bass._BassGuitar__make_6_strings()
    print(my_bass.details())

