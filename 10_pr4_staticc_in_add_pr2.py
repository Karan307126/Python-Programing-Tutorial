no=int(input("Enter the number:-"))

class Calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}.")

    def cube(self):
        print(f"THe value of {self.number} cube is {self.number **3}")

    def suareroot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")
   
    def cuberoot(self):
        print(f"The value of {self.number} cuberoot is {self.number **0.667}")

    @staticmethod
    def great():
        print("Hello User.")

a=Calculator(no)
a.great()
a.square()
a.cube()
a.cuberoot()
a.suareroot()