# TYPES OF  VARIABLES
# Instance Variable - variable defined inside init method
# Class(Static) Variable - outside init method

# TYPES OF  NAMESPACE
# Instance Namespace - where instance variables get created
# Class(Static) Namespace - class variables get created

class Car:

    wheels = 4 # Class variable

    def __init__(self) -> None:
        self.mileage = 12
        self.company = "BMW"
        # Here mileage and comp are Instance variables. At present they are constant but we can make it to change according to the object
        pass

c1 = Car()
c2 = Car()

c1.mileage = 8 # modifying instance variable

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)

Car.wheels = 3 # wheels being a class variable belongs to class namespace. So in order to work with wheels, to modify it, we have to use class name.

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)