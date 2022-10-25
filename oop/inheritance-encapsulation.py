class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play()  # it will automatically call this method whenever an instance is initialized

    def play(self):
        if self.n_strings == 6:
            print("6-string melody playing")
        else:
            print("Non 6-string melody")


if __name__ == '__main__':
    my_guitar = Guitar()
    print("There are", my_guitar.n_strings, "strings on this guitar")
    # my_guitar.play()
