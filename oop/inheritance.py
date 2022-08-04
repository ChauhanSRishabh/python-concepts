# INHERITANCE

class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

# A is Super Class and B is Sub Class

class B(A): # we will write B(A)
    # This means B is a Child Class/ Sub Class of A
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

A1 = A()
A1.feature1()
A1.feature2()

B1 = B()
B1.feature3()
B1.feature4()

# But what if you want to get the features of A as well?
# That is where inheritance comes into picture

# Accessing features of Class A with asn object of Class B(which is a sub class of A)
B1.feature1()


# MULTI-LEVEL INHERITANCE

class C(B): # C inherits B which inherits A. So it can access all

    def feature5(self):
        print("Feature 5 working")

c1 = C()

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()

# INHERITING MULTIPLE CLASSES

class ONE:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class TWO(): # we will write B(A)
    # This means B is a Child Class/ Sub Class of A
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class D(ONE, TWO): # Object of D can access methods of ONE and TWO both
    def feature(self):
        print("Feature working")

d1 = D()


d1.feature()
d1.feature1()
d1.feature2()
d1.feature3()
d1.feature4()
