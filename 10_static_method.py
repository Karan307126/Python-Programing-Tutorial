class Employee:
    companey = "Google"
    def getSalary(self,signeture):
        print(f"Salary for this employee working in {self.companey} is {self.salary}\n{signeture}")
    @staticmethod
    def greet():
        print("Good Morning,Sir")

karan=Employee()
karan.salary=1000000
karan.getSalary("Thanks!")    # Employee.getSalary(karan)
karan.greet()    # Employee.greet()