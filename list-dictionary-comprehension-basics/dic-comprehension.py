# some basic examples of how to use dictionary comprehension
# keep the idea of "easy to read" alive

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dict1.keys())  # it will print all keys
print(dict1.values())
print(dict1.items())  # both keys and values

double_dict1 = {k: v*2 for (k, v) in dict1.items()}  # iterate over key and value and double value in dict1
print("\nDict1 values doubled: ", double_dict1.values())

double_keys = {k*2: v for (k, v) in dict1.items()}
print("\nDoubled keys iterating over dict1", double_keys)

# note that we are storing a new dictionary based on an existing one

numbers = range(10)
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2  # the index will receive the double power of its value


# the same result could be achieved by implementing the following
new_dict_comp = {n: n ** 2 for n in numbers if n % 2 == 0}  # much simpler to read
