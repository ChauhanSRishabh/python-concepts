# OPERATOR OVERLOADING

a = 3
b = 7

print(a + b) # behind the scene, add() method shown in line 6 is getting called

print(int.__add__(a,b)) # add() is a method of class int

a = "Good"
b = "Boy"

print(str.__add__(a, b))

# Hence the moment you wite the '+' operator, it calls the add() method of respective class
# sub() for '-'
# mul() for '*'

# We call them Magic Methods


class Student:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2
        pass

    def __add__(self, other):
        m1 = self.m1+ other.m1
        m2 = self.m2+ other.m2
        s3 = Student(m1, m2)
        return s3
    
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if(s1>s2): # here s1 and s2 are integers
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'{self.m1} {self.m2}' # OR '{} {}'.format(self.m1, self.m2). Same thing!
        pass

s1 = Student(58,62)
s2 = Student(89, 90)

# EXAMPLE 1
s3 = s1 + s2 # TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
# BTS, add() method is called when '+' is encountered but we do not have that method for Student class
# So we need to OVERLOAD the operator of +
# Defining it : Line 26-30

print(s3.m1) # Output : 147

# EXAMPLE 2
if(s1>s2): # TypeError: '>' not supported between instances of 'Student' and 'Student'. Because it tries to call gt() method. So we need to Overload the > operator. See Lines 34-40
    print("s1 wins")
else:
    print("s2 wins")

# EXAMPLE 3
# print(s1) # Output : <__main__.Student object at 0x1026bffd0>. It is trying to call str() method
# print(s1.__str__()) # Gives same output as above because print(s1) is same as print(s1.__str__())

# So we need to overload the str() method to get our desired result. Lines 42 and 43
# It will return a tuple
print(s1) # TypeError: __str__ returned non-string (type tuple). 
# Converting it to tuple using f string