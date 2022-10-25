class Fruit:
    def __init__(self, name, color, weight):  # __init__ initializes an object, it works as a constructor
        self.name = name
        self.color = color
        self.weight = weight

    def get_weight(self):
        return self.weight

    def divide_weight_by_2(self):  # self is the keyword to reference that instance of class object
        return self.weight / 2

    def __str__(self):  # works much like a toString method in Java
        return f'It\'s a {self.name} and it\'s {self.color}'


if __name__ == '__main__':
    my_fruit = Fruit('kiwi', 'green', 100)
    print(my_fruit)
    print(my_fruit.get_weight())  # a way create a getter method
    print(my_fruit.divide_weight_by_2())  # it is converted to a float

    # note that it is expected that a number is passed into the weight variable in the __init__ function
    # if a string is passed, the programmer needs to cast it into a number value
