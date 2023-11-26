# Python does not by default abstraction.but we have import module ABC --> Abstract Base Class
from abc import *

class Computer:
    @abstractmethod
    def procces(self):
        pass

    @abstractmethod
    def cpu(self):
        pass

class Laptop(Computer):
    def procces(self):
        print("Proccesing...")
    def cpu(self):
        print("intel i core i5 11th gen")
    def memory(self):
        print("8gb ram and 4gb graphic card.")
    def storege(self):
        print("256gb SSD and 1tb HDD")


lap1 = Laptop()
lap1.procces()
lap1.storege()