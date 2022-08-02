# STRINGS

name = '''rishabh
is awesome''' # this is a multi-line string using ''', that were used for multi line comments as well

print(name[7]) # index 7 = 8th character, is a new-line and that will be printed

name = 'rishabh' # could have used " " as well, does not matter

print(name[2:5]) # last is not included, 5 won't come

print(name)
print(name.strip()) # will remove spaces from the beginning and the end

print(len(name))

var = name.lower()
print(var)
print(name.upper())
var = name.replace('s', 't') #rithabh
var = name.replace('sha', 'b') #ribbh
print(var)

name = 'rishabh, daddy, mummy'
var = name.replace(', ', '\n')
print(var)

stri = "This is a"
name = 'rishabh'
stri2 = "this is not a"
print(stri + name) # concatenate


# TEMPLATE AND FORMATTING
name1 = 'rishabh'
name2 = 'good boy'

template = "This is {} and he is a {}".format(name1, name2)
print(template)
template = "This is {0} and he is a {1}".format(name1, name2)
print(template)
template = "This is {1} and he is a {0}".format(name1, name2)
print(template)


# f-STRING
template = f"this is {name1} and he is a {name2}"
print(template)
