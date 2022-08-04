# POLYMORPHISM
# It means many(poly) forms(morph)

# Object will have lot of forms. One thing and multiple forms

# There are 4 ways of implementing polymorphism :
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overriding

# DUCK TYPING

# Duck Test : looks like a duck, swims like a duck, quacks like a duck, then it probably is a duck

x = 5 # you got a space of type int in your memory

x = "Rishabh" # now you are given a space of type string in the memory, x is just a name to it

class PyCharm():
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor():
    def execute(self):
        print("Spell-check")
        print("Auto-complete")
        print("Compiling")
        print("Running")

class Laptop():
    def code(self, ide): # I can change ide here. It doesn't matter what class' object you are passing as long as that class has a method with name that we are calling. In our case execute()
        ide.execute()

# ide = PyCharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

# If there is an object, i.e., ide and it has a method execute(), that's it. We are not concerned about which class object it is.