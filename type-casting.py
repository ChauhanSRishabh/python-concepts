
# type() function gives the type of a variable
typeA = type(a)
print(typeA) # output : <class 'int'>


e = "31"
print(type(e))

print(e+2) #error if e is "31"



# TYPE_CASTING
e = "31"
e = float(e)
print(e)
e = int(e)
print(e)
e = str(e)
print(e)
# e = int(3.65) # type-casted to the lower limit, not round off
print(2+int(e))
