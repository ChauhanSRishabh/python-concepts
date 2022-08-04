# CLASS INSIDE CLASS

class Student:
    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() # attribute that gets its value from another class
        # Creating object of inner class inside outer class 
        pass

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop: # INNER CLASS assigns all these 3 attributes to the instance through Line 7
        def __init__(self) -> None:
            self.brand = "Apple"
            self.ram = 8
            self.cpu = "M1"
            pass

        def show(self): # Both show methods are different
            print(self.brand, self.ram, self.cpu)

s1 = Student("Rishabh",75)
s2 = Student("B", 2)

# print(s1.name)

s1.show()

# Access attributes of inner class
print(s1.lap.brand)

# Assign it
lap1 = s1.lap
lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))

# Creating object of Inner class outside outer class
lap1 = Student.Laptop()

lap1.show()
s1.show()