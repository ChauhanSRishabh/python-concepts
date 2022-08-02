# TUPLES

# Different from list as we cannot change the elements in a tuple
# Tuple is unchangeable


'''
List mein [] but tuple mein ()
'''

a = ("rishabh", "asdf", "gh")
var = a
var = type(a)
print(a)  # Output was like this : ('rishabh', 'asdf', 'gh')
print(var)

# a[0] = "dad"  # Cannot do this. Gives an error as it is not allowed

# almost all the list methods are applicable. Search them


# We can type-cast a tuple into a list

a = list(a)
print(a) # Output changes : ['rishabh', 'asdf', 'gh']  Notice the change in brackets, from parentheses to square brackets
print(type(a))


# Now we can do 
a[0] = "dad"
print(a)