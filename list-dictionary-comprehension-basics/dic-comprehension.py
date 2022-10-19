# some basic examples of how to use dictionary comprehension
# keep the idea of "easy to read" alive

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("\nFirst some basics in dictionary operations:")
print("\nPrinting just the keys using the .keys() method: ", dict1.keys())  # it will print all keys
print("Printing just the values based on values() method: ", dict1.values())
print("The items() method returns both keys and values: ", dict1.items())  # both keys and values

double_dict1 = {k: v*2 for (k, v) in dict1.items()}  # iterate over key and value and double value in dict1
print("\nDict1 values doubled: ", double_dict1.values())

double_keys = {k*2: v for (k, v) in dict1.items()}
print("Doubled keys iterating over dict1:", double_keys)

# note that we are storing a new dictionary based on an existing one

numbers = range(10)
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2  # the index will receive the double power of its value


# the same result could be achieved by implementing the following
new_dict_comp = {n: n ** 2 for n in numbers if n % 2 == 0}  # much simpler to read

# converting fahrenheit temperatures to celsius using lamb
f = {'t1': -30,
     't2': -10,
     't3': 98,
     't4': 64}

# creating a list with the values provided by the f dictionary
celsius = list(map(lambda x: (float(5)/9) * (x-32), f.values()))
print("\nLet's print the list created into the celsius variable: ", celsius)
print("Remember: this list was created using a lambda function")
# float returns a float provided by number or string, if nothing is passed it fucking returns 0.0

# returning a dict that combines each element of the dict to the celsius list
c_dict = dict(zip(f.keys(), celsius)) # the zip() method will combine the keys with a given list
print("\nThe new dict bred from the zip() method into: ", c_dict)

# the same solution for the same problem using Dict Comp

f_comp = {'t1': 0, 't2': 100}
# iterate over two variables k, v, put keeping k as is and modifying v using the formula
c_comp = {k: (float(5)/9) * (v - 32) for (k, v) in f_comp.items()}
print("\nUsing dict comprehension: \n", c_comp)

# conditionals
# i will use dict1 from the beginning of this file for example
dict2 = {k: v for(k, v) in dict1.items() if v > 1}  # create a new dict with 2, 3, 4
print("\nUsing conditionals to create this dict: ", dict2)

# multiple ifs
dict3 = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}
print("\nA new dict was created using double conditional: ", dict3)

#if-else






