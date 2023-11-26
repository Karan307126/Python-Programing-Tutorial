class Employee:
    companey = "Google"
    def getSalary(self,signeture):
        print(f"Salary for this employee working in {self.companey} is {self.salary}\n{signeture}")
    
    def __init__(self,name,salary,subunit):
        print("Employee is created!")
        self.name=name
        self.salary=salary
        self.subunit=subunit
    
    def getDetails(self):
        print(f"The name of employee {self.name}")
        print(f"The salary of employee {self.salary}")
        print(f"The subunit of employee {self.subunit}")

    @classmethod
    def getcompaney(cls):
        print(f"This is class company {cls.companey}")

    @staticmethod
    def greet():
        print("Good Morning,Sir")
    
    @staticmethod
    def time():
        print("The time is 9am in the morning")

Employee.greet()
Employee.getcompaney()
karan=Employee("Karan",100000,"YouTube")
karan.getDetails()