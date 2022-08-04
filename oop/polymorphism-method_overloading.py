# METHOD OVERLOADING


class Student:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2
        pass

    def sum(self,a=None,b=None,c=None): # this method takes 2 arguments
        if(a!=None and b!= None and c!= None):
            s = a+b+c
        elif(a!=None and b!=None):
            s = a+b
        else:
            s=a
        return s

s1 = Student(58,62)
print(s1.sum(5,9))

# If we want to add 3 numbers, we need to create another method named sum that takes 3 arguments. This is how we do it in other languages
# But here we'll not do that. It is not supported in python
# We can use 3rd variable and we can be passing 3 arguments and accepting 3 arguments

# But what if we don't pass 3 arguments?
# Set all the arguments to be 'None' by default and add a check, Lines 11-16