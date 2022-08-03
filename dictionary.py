# DICTIONARY

# Key-Value Pairs

from operator import le


Dict = {
    "name" : 'rishabh',
    "degree" : "b.tech",
    "percent" : 80,
}

print(Dict) # {'name': 'rishabh', 'degree': 'b.tech', 'percent': 80}

# print(Dict[0]) # KeyError: 0. You have to give the key, not the index

print(Dict["percent"]) # Output : 80

# UPDATE vale at a particular key
Dict["percent"] = 90
print(Dict)

# UPDATE METHOD to update the dictionary
add = {"Grade" : "A"}
Dict.update(add) # add will be added to the end of Dict
print(Dict)

# LENGTH
print(len(Dict))

#POP
print(Dict.pop("percent"))
print(Dict)
# print(Dict.pop()) Pop won't work without argument, you have to give key as argument

# DELETE
# cannot use del to remove element with a particular key
del Dict
print(Dict)