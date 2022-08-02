''' PYTHON COLLECTIONS
1. List
2. Tuple
3. Set
4. Dictionary
'''

# LIST METHODS : https://www.geeksforgeeks.org/list-methods-in-python/


# List is just like an array

lst = [61,2,3,4,6,41]
var = type(lst)
print(lst)
print(var)

# Everything in python is an object of a class
# lst is an object of class list

element = lst[1]
print(element)
element = lst[1:4]
print(element)

# MODIFICATIONS/ UPDATIONS

lst[2] = 45 # element at index 2, i.e., 3 is replaced by 45
var = lst
print(lst)
print(var) 

# LENGTH
var = len(lst)
print(var)

# ADDING ELEMENT AT END
lst.append(34)
print(lst)

# INSERTING AT A PARTICULAR POSITION
lst.insert(1, 100)
print(lst)

# REMOVING A PARTICULAR ELEMENT
lst.remove(61)
print(lst)

# POP function -> Removes and returns the last value from the List or the given index value.
lst.pop() #Removing from the end
lst.pop(2) # Removing from index 2
print(lst)

# DELETE AT A PARTICULAR INDEX
del lst[3] # delete at index 3
print(lst)

# CLEAR FUNCTION
lst.clear() # list is cleared, all elements are removed but list named lst exists
print(lst)

# DELETE LIST ALTOGETHER
del lst # list named lt is deleted, nothing exists
print(lst)
