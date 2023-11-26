# This is single Inheritance .

class Employee:
    company="Google"
    
    def showDteils(self):
        print("This is an Employee.")

class Programmer(Employee):
    language="Python"
    company="YouTube"

    def getLanguage(self):
        print(f"The language is {self.language}.")

    def showDteils(self):
        print("This is a programmer.")

e=Employee()
e.showDteils()
p=Programmer()
p.showDteils()
print(p.company)
print(e.company)