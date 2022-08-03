# OBJECT ORIENTED PROGRAMMING

# CLASS AND OBJECTS
class Computer:
    def config(self): # METHOD INSIDE CLASS
        print("M1", "8GB RAM", "256GB SSD")

com1 = Computer() # Object of class computer. It will have some attributes(variables) and a behaviour(basically methods, in oops we call functions as methods)
# config is a method inside class computer and it is he behaviour of com1

# Both will give same output
Computer.config(com1) # if we remove com1, it will give an error
# config() missing 1 required positional argument: 'self'
com1.config()

