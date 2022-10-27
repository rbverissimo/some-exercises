import random


def print_a_list(some_list):
    for i in some_list:
        print(i)


def return_10_random_numbers_between_0_and_1000():
    list_of_nums = []
    for _ in range(10):
        num = random.randint(0, 1000)
        list_of_nums.append(num)
    return list_of_nums


if __name__ == '__main__':
    print_a_list(["VW Beetle", "Honda Civic", "Porsche 911"])
    print(return_10_random_numbers_between_0_and_1000())

