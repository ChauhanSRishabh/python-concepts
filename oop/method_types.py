# TYPES OF METHOD
# Instance Method
# Class Method
# Static Method

#  For variables, Class and Static were same but that is not the case with methods

class Student:

    school = "PBD"

    def __init__(self, marks1, marks2, marks3) -> None:
        self.m1 = marks1
        self.m2 = marks2
        self.m3 = marks3
        pass

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    def get_marks1(self):
        return self.m1
    
    def set_marks1(self, value):
        self.m1 = value

    @classmethod #Line 54 & 59
    def getschoolname(cls):
         return cls.school

    @staticmethod # Line 55
    def info(): # Neither do we have self nor cls inside () as it is not related to either of them
        print("This is Student Class....in oop module")
         

s1 = Student(90, 91, 95)
s2 = Student(54, 67, 89)

print(s1.avg())
print(s2.avg())

'''
INSTANCE METHOD

m1, m2, m3 are instance variables and can be used with instance methods. Here avg() is an Instance Method as it works with the instance variables of objects s1 and s2

In Instance Methods, we have types:
1. Accessor Methods - fetch the values -> GETTERS
2. Mutator Methods - modify the values -> SETTERS
''' 

# IMPORTANT
# If you are working with instance variables, use self keyword, no decorator
# When working with class variables, use cls keyword as in Line 28 and decorator : @classmathod
# When we do not need to work with class or instance variables, use neither of self or cls keywords, only decorator : @staticmethod

# CLASS METHOD
print(Student.getschoolname()) # TypeError: getschoolname() missing 1 required positional argument: 'cls'
# we need to use a decorator @classmethod if we want to use getschoolname as a class method

# STATIC METHOD
print(Student.info())