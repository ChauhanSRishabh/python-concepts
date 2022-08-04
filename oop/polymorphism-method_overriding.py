# METHOD OVERRIDING

# Heavily used concept in Software industry
# Interfaces, abstract classes

class A:
    def show(self):
        print("In A show")

class B(A):
    def show(self):
        print("In B's show")
    pass

a1 = A()
a1.show()

a1 = B()
a1.show() # AttributeError: 'B' object has no attribute 'show'
# Will run if we write B(A)

# But if we write a show method for B as well(Lines 11, 12), then the show() method of B overrides show() of A