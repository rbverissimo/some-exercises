class Guitar:
    def __init__(self):
        self.n_strings = 6
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
        self.n_strings = 8
        self.play()  # using this method without taking it from the super()


class BassGuitar(Guitar):
    def __init__(self):
        super().__init__()  # it will first initialize attributes and methods biased by that parent class
        self.n_strings = 4


if __name__ == '__main__':
    my_guitar = Guitar()
    print("There are", my_guitar.n_strings, "strings on this guitar")
    # my_guitar.play()
    print("\nJust got my bass guitar: ")
    my_bass = BassGuitar()
    my_bass.details()

    print("\nJust got an 8-stringed guitar:")
    my_8_strings = ElectricGuitar()
