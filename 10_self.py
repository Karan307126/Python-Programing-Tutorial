class Employee:
    companey = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.companey} is {self.salary}")

karan=Employee()
karan.salary=1000000
karan.getSalary()
Employee.getSalary(karan)