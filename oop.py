# OBJECT ORIENTED PROGRAMMING

class Employee:
    def __init__(self, name, salary) -> None:  # __init__ method is the Python equivalent of the C++ constructor
        self.name = name
        self.salary = salary
        pass

rishabh = Employee("rishabh", "12 lakh")

print(rishabh.name)
print(rishabh.salary)