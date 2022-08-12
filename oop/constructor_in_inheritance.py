# CONSTRUCTOR IN INHERITANCE

# Inheritance is using features of existing classes

'''
class A:

    def __init__(self) -> None:
        print("In A init")
        pass

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):

    # def __init__(self) -> None:
    #     print("in B init")

    def __init__(self) -> None:
        super().__init__() # To represent the super class, we use super method, hence this line will call init method of class A
        print("In B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

# a1 = A() # As soon as we write A(), it acts as our constructor and calls __init__ method, even if we don't define it, it is there somewhere

# What if we create object of B
a1 = B() # Will it call the constructor of A? Yes it wil. Output : init of A
# Why? Because up until now, we don't have init for B, so it goes to init of A
# What if we had init in B as well? Then it will go to init of B


# A is superclass and B is sub class
# Sub class can access all the methods of super class but not vice-versa.


# IMP
# If  you create an object of sub class, it will first try to find init of sub class. If not found, then it calls init of super class

# What if we want to call init of A as well?
# Commenting lines 20 and 21
# See init method in Line 23
# On line 24, as soon as we write 'super().' we can access all the methods of the Super class A

# Now when we write 
a1 = B()
# Output : 
# In A init
# In B init
'''

# What if a class has more than 1 super class

class A:

    def __init__(self) -> None:
        print("In A init")
        pass

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

class B():

    def __init__(self) -> None:
        print("In B init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):

    def __init__(self) -> None:
        super().__init__()
        print("In C init")
        pass

c1 = C()

'''
OUTPUT
In A init
In C init
'''

# Why A's init was called and not B's when we wrote super().__init__() on Line 88?

# METHOD RESOLUTION ORDER(MRO)
# Whenever we have multiple inheritance, it always starts from left to right. So the moment we wrote super().__init__(), it prefers left one.

# Same for methods
# We have two methods in A and B respectively with same name feature1()
# When we call feature1, always a will be preferred because of MRO
c1.feature1()
