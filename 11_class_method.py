class Employee:
    company="Camel"
    salary=100
    location="Ahmedabad"

    # def changeSalary(self,sal):
    #     self.__class__.salary=sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(445)
print(e.salary)
print(Employee.salary)