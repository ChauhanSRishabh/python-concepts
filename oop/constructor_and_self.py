
# CONSTRUCTORS AND SELF

# class Computer:
#     pass # paas is used here to keep class as empty, without it error would have occurred


# c1 = Computer() # Object c1 created in heap
# print(id(c1)) # Address of the memory where object c1 was created

# c2 = Computer()
# print(id(c2)) 

# Every time we run our script, the above objects, c1 and c2 will take 2 different memory locations

'''
Size of the object? How much size will it acquire?
Depends on the number of variables and size of each variable
'''

'''
Who allocates size to object? Who calculates the memory require d?
CONSTRUCTOR
eg : Computer() is our constructor
whenever you write a constructor, it will call the __init__ method internally
'''

'''
self

The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
'''

class Computer:
    def __init__(self) -> None:
        # Creating variable/attribute inside/of an object
        # name and age
        self.name = "Rishabh"
        self.age = 27 
        pass

    def update(self): # self is basically a pointer to the object that is calling this method. In our case, line 51 : c1.update(), self points to c1
        self.age = 30
    
    def compare(self, other): # Line 54 : c1 becomes self and c2 becomes other
        if self.age == other.age:
            return True
        else:
            return False


c1 =  Computer()
c2 =  Computer()

print(c1.name)
print(c2.name)

# update method
# c1.update()

# compare method to compare objects
if c1.compare(c2):
    print("They are same")

# Change name and age
c1.name = "Dad"
c1.age = 56

print(c1.name)
print(c1.age)