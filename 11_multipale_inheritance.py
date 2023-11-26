class Employee:
    company="Visa"
    eCode=120

class Freelancer:
    company="Fiverr"
    leavel=0

    def upgradeLeavel(self):
        self.leavel=self.leavel+1

class Programmer(Employee,Freelancer):
    name="Karan"

p=Programmer()
p.upgradeLeavel()
print(p.leavel)
print(p.company)