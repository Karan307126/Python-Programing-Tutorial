class Employee:
    company="Bharat Gas"
    salary=5600
    salarybonus= 400   # int(input("Enteer the salarybonus:-"))

    @property    # this is getter 
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val-self.salary

e=Employee()
print(e.totalSalary)
e.totalSalary=5800
print(e.salary)
print(e.salarybonus)