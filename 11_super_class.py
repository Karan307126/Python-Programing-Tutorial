class Person:
    country="India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company="Honda"
    # def getSalary(self):
    #     print(f"Salary is {self.salary}")
        
    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am lucily breathing...")

class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print(f"No salarry to programmers.")

    def takeBreath(self):
        super().takeBreath()
        print("I am Programmer so I am brithing ++...")

p=Person()
p.takeBreath()
e=Employee()
e.takeBreath()
pr=Programmer()
pr.takeBreath()