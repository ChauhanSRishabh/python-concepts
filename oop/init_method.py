# THE __init__ METHOD

class Computer:

    def __init__(self, cpu, ram) -> None: # Special method, called internally by the CONSTRUCTOR, automatically
    # cpu and ram are arguments
    # object here is self
        # print("in init")
        self.processor = cpu # to assign arguments to the object attribute
        self.memory = ram
        pass

    def config(self):
        print("Config is", self.processor, self.memory)

com1 = Computer("M1", "8GB")
com2 = Computer("i5", "16GB")

print(com1.processor) # processor is attribute(variable) of com1. M1 will get printed

com1.config()
com2.config()