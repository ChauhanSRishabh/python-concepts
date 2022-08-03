# FOR LOOP

# for i in range(0,1000):
    # print(i+1);

# for in List
li = [2,3,4,5,6,7,8]
# iterate an entire list using for loop
for item in li:
    print(item)

print() # to add a line in between

# for in Tuples
tup = ("a","b","c","d")
for item in tup:
    print(item)

print()

# for in Sets
set1 = {1,2,3,4,3,2,1,4,5,6,7,8}
for item in set1:
    print(item) # no repetition of elements as

print()

# for in Dictionary
dict = {
    1 : "rishabh",
    "nickname" : "stud",
    3 : "rich",
    4 : "coder"
}
for item in dict:
    print(item) # will print the key, which can be of any datatype
    print(dict[item]) # will print the value at each key

print()

# WHILE LOOP
# DO WHILE LOOP