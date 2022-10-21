# some operations that with lists, dataframes and dicts

names = ['Renato', 'Gandalf', 'Mariana']
profs = ['Developer', 'Product Owner', 'QA']

# zipping both lists together based on index, creating a dict
dict_names_profs = {}

for(key, value) in zip(names, profs):
    dict_names_profs[key] = value

print("\nDictionary created using a for loop and the zip function: ", dict_names_profs)

dict_names_profs = {k: v for (k, v) in zip(names, profs)}  # the comprehension way to do it
print("\nNow with the comprehension feature, same result: ", dict_names_profs)

# now it is possible to do the same operation using a range() function
new_dict_names_profs = {}

for i in range(3):  # or range(len(names)) for example
    new_dict_names_profs[names[i]] = profs[i]

print("\nBasically the same operation but using the range(): ", new_dict_names_profs)

# the comprehension with range:
new_dict_names_profs = {names[i]: profs[i] for i in range(len(names))}
print("\nUsing the range func with the comprehension feature: ", new_dict_names_profs)


