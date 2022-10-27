import random


# recursion is a function that call itself

def catch_9():
    random_number = random.randint(0, 9)
    if random_number == 9:
        return random_number
    else:
        print(random_number)
        catch_9()


def even_numbers(list_of_numbers):
    list_temp = list_of_numbers
    list_of_evens = []
    for i in list_temp:
        if i % 2 == 0:
            list_of_evens.append(i)

    return list_of_evens


def recursive_evens(num):
    if num % 2 == 0:
        list_of_nums.append(num)
        if num == 2:
            return num
        else:
            return recursive_evens(num-2)
    else:
        return recursive_evens(num-1)


if __name__ == '__main__':
    catch_9()
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(even_numbers(nums_list))
    list_of_nums = []
    print(recursive_evens(10))
