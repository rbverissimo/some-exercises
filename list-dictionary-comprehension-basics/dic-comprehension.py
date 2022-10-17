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

